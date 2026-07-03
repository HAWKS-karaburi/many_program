"""
파일 자동 정리기 (File Organizer)
- 확장자를 '카테고리'로 묶어서 폴더별로 자동 분류
- customtkinter 기반 GUI + 부드러운 애니메이션
- PyInstaller로 exe 배포 가능

작성: Claude-Haiku 4.5
"""

import os
import shutil
import threading
import time
from pathlib import Path

import customtkinter as ctk
from tkinter import filedialog, messagebox

# ------------------------------------------------------------
# 1. 카테고리 정의 : 확장자 -> 카테고리 폴더명
#    (단순 확장자별이 아니라 '의미'로 묶음)
# ------------------------------------------------------------
CATEGORY_MAP = {
    "문서": [".doc", ".docx", ".pdf", ".txt", ".hwp", ".hwpx", ".ppt",
             ".pptx", ".xls", ".xlsx", ".rtf", ".odt", ".csv", ".md"],
    "이미지": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp",
              ".tiff", ".tif", ".ico", ".heic", ".raw"],
    "동영상": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm",
              ".m4v", ".mpg", ".mpeg"],
    "음악": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "압축파일": [".zip", ".rar", ".7z", ".tar", ".gz", ".alz", ".egg", ".bz2"],
    "바로가기": [".lnk", ".url", ".webloc"],
    "실행파일": [".exe", ".msi", ".bat", ".sh", ".app", ".cmd", ".jar"],
    "코드": [".py", ".cpp", ".c", ".h", ".java", ".js", ".ts", ".jsx",
            ".tsx", ".html", ".css", ".json", ".xml", ".sql", ".ipynb",
            ".go", ".rs", ".php"],
    "폰트": [".ttf", ".otf", ".woff", ".woff2"],
    "디스크이미지": [".iso", ".img", ".dmg"],
    "폴더(디렉터리)": [],  # 특수 처리
}

# 확장자 -> 카테고리 역인덱스 생성
EXT_TO_CATEGORY = {}
for category, exts in CATEGORY_MAP.items():
    for ext in exts:
        EXT_TO_CATEGORY[ext] = category

FALLBACK_CATEGORY = "기타"


def classify(path: Path) -> str:
    """파일(또는 폴더) 하나를 어떤 카테고리로 보낼지 결정"""
    if path.is_dir():
        return None  # 폴더는 건드리지 않음 (이미 정리된 카테고리 폴더 포함)
    ext = path.suffix.lower()
    return EXT_TO_CATEGORY.get(ext, FALLBACK_CATEGORY)


# ------------------------------------------------------------
# 2. GUI 애플리케이션
# ------------------------------------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("파일 자동 정리기")
        self.geometry("640x560")
        self.minsize(560, 480)

        # ---- 페이드인 애니메이션을 위해 처음엔 투명하게 시작 ----
        self.attributes("-alpha", 0.0)

        self.target_folder = ctk.StringVar(value="")
        self.include_subfolders = ctk.BooleanVar(value=False)
        self.dry_run = ctk.BooleanVar(value=False)
        self.is_running = False

        self._build_ui()
        self._fade_in()

    # ---------------------------------------------------------
    # UI 구성
    # ---------------------------------------------------------
    def _build_ui(self):
        pad = {"padx": 20, "pady": 8}

        title_label = ctk.CTkLabel(
            self, text="📂 파일 자동 정리기",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(20, 4))

        subtitle = ctk.CTkLabel(
            self,
            text="확장자를 문서·이미지·동영상·바로가기 등 '의미 단위'로 분류해줘요",
            font=ctk.CTkFont(size=12),
            text_color="gray70",
        )
        subtitle.pack(pady=(0, 10))

        # ----- 폴더 선택 영역 -----
        folder_frame = ctk.CTkFrame(self)
        folder_frame.pack(fill="x", **pad)

        self.folder_entry = ctk.CTkEntry(
            folder_frame, textvariable=self.target_folder,
            placeholder_text="정리할 폴더 경로를 선택하세요"
        )
        self.folder_entry.pack(side="left", fill="x", expand=True,
                                padx=(12, 8), pady=12)

        browse_btn = ctk.CTkButton(
            folder_frame, text="폴더 선택", width=100,
            command=self._browse_folder
        )
        browse_btn.pack(side="right", padx=(0, 12), pady=12)

        # ----- 옵션 영역 -----
        option_frame = ctk.CTkFrame(self)
        option_frame.pack(fill="x", **pad)

        sub_check = ctk.CTkCheckBox(
            option_frame, text="하위 폴더까지 포함해서 정리",
            variable=self.include_subfolders
        )
        sub_check.pack(side="left", padx=12, pady=10)

        dry_check = ctk.CTkCheckBox(
            option_frame, text="미리보기만 (실제로 이동 안 함)",
            variable=self.dry_run
        )
        dry_check.pack(side="left", padx=12, pady=10)

        # ----- 시작 버튼 -----
        self.start_btn = ctk.CTkButton(
            self, text="정리 시작", height=44,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._start_organizing
        )
        self.start_btn.pack(fill="x", padx=20, pady=(6, 10))

        # ----- 진행바 (부드러운 애니메이션 적용) -----
        self.progress_bar = ctk.CTkProgressBar(self, height=16)
        self.progress_bar.set(0)
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 6))

        self.progress_label = ctk.CTkLabel(self, text="대기 중...",
                                            font=ctk.CTkFont(size=12))
        self.progress_label.pack(pady=(0, 10))

        # ----- 로그 박스 -----
        self.log_box = ctk.CTkTextbox(self, font=ctk.CTkFont(size=12))
        self.log_box.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.log_box.configure(state="disabled")

    # ---------------------------------------------------------
    # 페이드인 애니메이션 (창이 서서히 나타남)
    # ---------------------------------------------------------
    def _fade_in(self, alpha=0.0):
        alpha += 0.06
        if alpha >= 1.0:
            self.attributes("-alpha", 1.0)
            return
        self.attributes("-alpha", alpha)
        self.after(15, lambda: self._fade_in(alpha))

    # ---------------------------------------------------------
    # 진행바를 목표값까지 부드럽게 채우는 애니메이션
    # ---------------------------------------------------------
    def _animate_progress(self, target: float, current: float = None):
        if current is None:
            current = self.progress_bar.get()
        step = (target - current) * 0.25
        if abs(target - current) < 0.002:
            self.progress_bar.set(target)
            return
        new_val = current + step
        self.progress_bar.set(new_val)
        self.after(12, lambda: self._animate_progress(target, new_val))

    # ---------------------------------------------------------
    # 로그 출력
    # ---------------------------------------------------------
    def _log(self, message: str):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    # ---------------------------------------------------------
    # 폴더 선택 다이얼로그
    # ---------------------------------------------------------
    def _browse_folder(self):
        folder = filedialog.askdirectory(title="정리할 폴더를 선택하세요")
        if folder:
            self.target_folder.set(folder)

    # ---------------------------------------------------------
    # 정리 시작 (백그라운드 스레드로 실행 -> UI 안 멈춤)
    # ---------------------------------------------------------
    def _start_organizing(self):
        if self.is_running:
            return

        folder = self.target_folder.get().strip()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("경고", "올바른 폴더를 먼저 선택해줘!")
            return

        self.is_running = True
        self.start_btn.configure(state="disabled", text="정리 중...")
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self._animate_progress(0.0, self.progress_bar.get())
        self.progress_bar.set(0)

        thread = threading.Thread(target=self._organize_worker, args=(folder,), daemon=True)
        thread.start()

    # ---------------------------------------------------------
    # 실제 파일 정리 로직 (별도 스레드)
    # ---------------------------------------------------------
    def _organize_worker(self, folder: str):
        root = Path(folder)
        include_sub = self.include_subfolders.get()
        preview_only = self.dry_run.get()

        # 대상 파일 목록 수집 (이미 만들어진 카테고리 폴더는 스킵)
        category_names = set(CATEGORY_MAP.keys()) | {FALLBACK_CATEGORY}

        if include_sub:
            all_paths = [p for p in root.rglob("*") if p.is_file()]
        else:
            all_paths = [p for p in root.iterdir() if p.is_file()]

        # 이미 카테고리 폴더 안에 있는 파일은 제외
        all_paths = [
            p for p in all_paths
            if p.parent.name not in category_names or p.parent == root
        ]

        total = len(all_paths)
        if total == 0:
            self.after(0, lambda: self._log("정리할 파일이 없어."))
            self.after(0, self._finish)
            return

        moved_count = 0
        self.after(0, lambda: self._log(f"총 {total}개 파일 발견. 분류를 시작할게.\n"))

        for idx, file_path in enumerate(all_paths, start=1):
            category = classify(file_path)
            if category is None:
                continue

            dest_dir = root / category
            dest_path = dest_dir / file_path.name

            if preview_only:
                self.after(0, lambda f=file_path.name, c=category:
                           self._log(f"[미리보기] {f}  ->  {c}/"))
            else:
                try:
                    dest_dir.mkdir(exist_ok=True)
                    # 이름 중복되면 (1), (2) 붙여서 저장
                    dest_path = self._resolve_conflict(dest_path)
                    shutil.move(str(file_path), str(dest_path))
                    moved_count += 1
                    self.after(0, lambda f=file_path.name, c=category:
                               self._log(f"✔ {f}  ->  {c}/"))
                except Exception as e:
                    self.after(0, lambda f=file_path.name, err=e:
                               self._log(f"✘ {f} 이동 실패: {err}"))

            progress = idx / total
            self.after(0, lambda p=progress: self._animate_progress(p))
            self.after(0, lambda i=idx, t=total:
                       self.progress_label.configure(text=f"{i}/{t} 처리 중..."))
            time.sleep(0.01)  # 애니메이션이 부드럽게 보이도록 살짝 텀

        summary = (f"\n완료! 총 {total}개 중 {moved_count}개 이동함."
                   if not preview_only else f"\n미리보기 완료 ({total}개 대상).")
        self.after(0, lambda: self._log(summary))
        self.after(0, self._finish)

    @staticmethod
    def _resolve_conflict(dest_path: Path) -> Path:
        """같은 이름 파일이 이미 있으면 '이름 (1).ext' 형태로 바꿔줌"""
        if not dest_path.exists():
            return dest_path
        stem, suffix = dest_path.stem, dest_path.suffix
        parent = dest_path.parent
        counter = 1
        new_path = parent / f"{stem} ({counter}){suffix}"
        while new_path.exists():
            counter += 1
            new_path = parent / f"{stem} ({counter}){suffix}"
        return new_path

    def _finish(self):
        self.is_running = False
        self.start_btn.configure(state="normal", text="정리 시작")
        self.progress_label.configure(text="완료!")


if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()
