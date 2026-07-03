# 📂 파일 자동 정리기 (File Organizer)

확장자를 **"문서", "이미지", "동영상"** 같이 의미 단위로 묶어서 폴더를 자동 생성하고 파일을 분류해주는 프로그램입니다.

## ✨ 특징

- 🎯 **스마트한 카테고리 분류**: 확장자별이 아니라 의미별 분류
  - 문서, 이미지, 동영상, 음악, 압축파일, 바로가기, 실행파일, 코드, 폰트, 디스크이미지, 기타
  
- 🎨 **예쁜 GUI**: customtkinter 기반 다크모드 인터페이스
  
- 🎬 **부드러운 애니메이션**
  - 창이 서서히 나타나는 페이드인 효과
  - 진행바가 자연스럽게 차오르는 이징 애니메이션
  
- ⚡ **논블로킹 UI**: 대량 파일도 창이 멈추지 않음 (멀티스레딩)
  
- 🔒 **안전한 동작**
  - 중복 파일은 자동으로 `(1)`, `(2)` 붙여서 덮어쓰기 방지
  - "미리보기" 모드로 실제 이동 전에 확인 가능

---

## 🚀 사용 방법

### 1️⃣ 개발 환경에서 직접 실행

```bash
pip install -r requirements.txt
python file_organizer.py
```

### 2️⃣ exe 파일로 배포 (Windows)

#### **방법 A: Python 스크립트로 빌드 (추천) ⭐**

```bash
python build.py
```

→ `dist/FileOrganizer.exe` 가 생성돼요.

#### **방법 B: 명령어로 직접 빌드**

```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --name FileOrganizer --collect-all customtkinter file_organizer.py
```

---

## 📋 프로그램 사용법

| 항목 | 설명 |
|------|------|
| **폴더 선택** | "폴더 선택" 버튼으로 정리하고 싶은 폴더 지정 |
| **하위 폴더까지 포함** | 선택하면 서브폴더 내의 파일도 함께 정리 |
| **미리보기만** | 체크하면 실제로 이동하지 않고 로그만 보여줌 |
| **정리 시작** | 버튼 클릭하면 자동 분류 시작 (백그라운드 스레드 실행) |

---

## 📁 분류 카테고리

```
원본 폴더/
├── 문서/           (doc, docx, pdf, txt, hwp, ppt, xls, csv 등)
├── 이미지/         (jpg, png, gif, bmp, svg, webp 등)
├── 동영상/         (mp4, avi, mkv, mov, wmv, webm 등)
├── 음악/           (mp3, wav, flac, aac, ogg, m4a 등)
├── 압축파일/       (zip, rar, 7z, tar, gz, alz 등)
├── 바로가기/       (lnk, url, webloc)
├── 실행파일/       (exe, msi, bat, sh, jar 등)
├── 코드/           (py, cpp, c, java, js, html, css, json 등)
├── 폰트/           (ttf, otf, woff)
├── 디스크이미지/   (iso, img, dmg)
└── 기타/           (위의 어디에도 해당 안 하는 파일들)
```

---

## 🛠️ 커스터마이징

### 카테고리 추가/변경하기

`file_organizer.py` 파일의 `CATEGORY_MAP` 딕셔너리를 수정하면 돼요:

```python
CATEGORY_MAP = {
    "문서": [".doc", ".docx", ".pdf", ".txt", ".hwp", ...],
    "이미지": [".jpg", ".jpeg", ".png", ...],
    "게임세이브": [".sav", ".dat"],  # ← 새로운 카테고리 추가!
    ...
}
```

### 색상 테마 바꾸기

```python
ctk.set_appearance_mode("light")  # "dark" 또는 "light"
ctk.set_default_color_theme("green")  # "blue", "green", "dark-blue" 등
```

---

## 💾 배포 후 실행

### exe 파일을 Windows에서 바탕화면 바로가기로 만들기

1. `dist/FileOrganizer.exe` 마우스 우클릭
2. "바로가기 만들기" 선택
3. 생성된 바로가기를 **바탕화면**으로 이동

### 폴더에서 바로 실행하기

`build.py` 가 완성되면 `dist` 폴더 안의 `FileOrganizer.exe` 를 자유롭게 옮겨서 사용하면 돼.

---

## 🐛 문제 해결

### "customtkinter not found" 오류
```bash
pip install customtkinter
```

### "pyinstaller not found" 오류
```bash
pip install pyinstaller
```

### exe 빌드가 안 될 때
- Python 3.8+ 사용하고 있는지 확인
- 폴더명에 특수문자 없는지 확인
- `pip install --upgrade pip` 로 pip 최신화 후 재시도

---

## 📦 파일 구조

```
.
├── file_organizer.py    # 메인 프로그램
├── build.py             # exe 빌드 스크립트
├── requirements.txt     # 필요 패키지 목록
└── README.md           # 이 파일
```

---

## 🎓 기술 스택

- **Python 3.8+**
- **customtkinter** - 모던한 GUI 라이브러리
- **PyInstaller** - Python을 exe로 패키징
- **threading** - 멀티스레딩으로 UI 블로킹 방지

---

## 📝 라이선스

자유롭게 개인/기업용으로 사용 가능합니다.

---

## 💡 팁

- 정리 전에 **"미리보기만"** 체크해서 먼저 어떻게 분류될지 확인하고 진행하면 안전해요
- 정리된 폴더는 다시 한 번 실행해도 이미 만들어진 카테고리 폴더 안의 파일들은 건드리지 않아요 (안전성 확보)
- 대량 파일(1000개+)일 때도 UI가 부드럽게 반응해요

---

**Made with ❤️ by Claude**
