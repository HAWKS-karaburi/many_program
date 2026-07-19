# 틱택토 (Tic-Tac-Toe)

간단한 콘솔 기반 틱택토(3x3) 게임입니다.
- 언어: C++ (C++20)
- 위치: Pacto7107/틱택토

기능
- 플레이어 vs 플레이어
- 플레이어 vs 간단한 AI(승리/막기 우선, 중앙 우선, 무작위)
- 빌드: CMake (C++20)

빌드 & 실행

1. 빌드
```bash
mkdir -p build && cd build
cmake .. && cmake --build .
```

2. 실행
```bash
# 실행 파일: Pacto7107/틱택토/build/tictactoe
./tictactoe
```

게임 조작
- 보드는 3x3으로 좌표는 행(1-3)과 열(1-3)로 입력합니다. 예: 2 3 -> 2행 3열
- 실행 후 모드를 선택하세요: 1) 플레이어 vs 플레이어  2) 플레이어 vs AI

테스트 데모
- tests/run_demo.sh에는 빌드 후 실행 예시가 포함되어 있습니다.

파일 구조
```
Pacto7107/틱택토/
├─ CMakeLists.txt
├─ README.md
├─ src/
│  └─ main.cpp
└─ tests/
   └─ run_demo.sh
```

원하시면:
- AI를 강화(minimax)하거나
- ncurses 인터페이스를 추가하거나
- 단위 테스트(Catch2 등)를 추가해드릴 수 있습니다.
