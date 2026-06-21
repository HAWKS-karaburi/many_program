// idea by Pacto7107
// thanks by gemini
// it made make move, win ck func and utf8 print

#include <iostream>
#include <algorithm>
#include <string>
////
#include <windows.h>
////
// Sleep(밀리초)
// system("cls")
//// □ ■ ▣
#define fr(i,s,e) for(int (i) = (s); (i) < (e); (i)++)
#define bd(x,i) board[(x)][(i)]
#define wait Sleep(200)
using ll = long long;

using namespace std;
string board[9][8]; // [x][i], x = 1부터, x번째 열에 아래 i 번째 칸;
// 가로, 세로
string now_pl;

void Console_update() {
    system("cls");
    for (int j = 6; j >= 1; j--) {
        for (int i = 1; i <= 7; i++) {
            cout << board[i][j];
        }
        cout << '\n';
    }
}
void First_set() {
    for (int i = 1; i <= 7; i++) {
        for (int j = 6; j >= 1; j--) {
            board[i][j] = "□";
        }
    }
    Console_update();
}
//// □ ■ ▣
int Make_move(int x) {
    int rtn = 1; // 기본 바닥 위치

    // 위에서부터 아래로 내려가며 빈칸을 찾음
    for (int i = 6; i >= 1; i--) {
        // 만약 아래 칸(i-1)에 이미 돌이 있거나, 현재가 맨 바닥(i==1)이라면 정착!
        if (i == 1 || board[x][i - 1] != "□") {
            board[x][i] = now_pl;
            Console_update();
            rtn = i; // 돌이 멈춘 정확한 층수(i)를 기록!
            break;
        }

        // 아직 공중에 떠 있는 상태라면 낙하 애니메이션 연출
        board[x][i] = now_pl;
        Console_update();
        wait;
        board[x][i] = "□"; // 다음 칸으로 가기 전 현재 칸 비우기
    }

    return rtn; // 이제 정확히 돌이 안착한 높이를 반환합니다!
}

bool Win_ck(int x, int i) {
    int dx[4] = { 1, 1, 0, -1 };
    int dy[4] = { 0, 1, 1,  1 };

    // 4가지 축(가로, 대각선2, 세로) 검사
    for (int d = 0; d < 4; d++) {
        // 승리한 돌들의 좌표를 저장할 배열 (최대 7목까지 가능하므로 여유있게 10칸)
        pair<int, int> win_stones[10];
        int count = 0;

        // 현재 놓은 돌 저장
        win_stones[count++] = { x, i };

        // 1. 정방향 조사
        int tx = x + dx[d];
        int ty = i + dy[d];
        while (tx >= 1 && tx <= 7 && ty >= 1 && ty <= 6 && board[tx][ty] == now_pl) {
            win_stones[count++] = { tx, ty };
            tx += dx[d];
            ty += dy[d];
        }

        // 2. 역방향 조사
        tx = x - dx[d];
        ty = i - dy[d];
        while (tx >= 1 && tx <= 7 && ty >= 1 && ty <= 6 && board[tx][ty] == now_pl) {
            win_stones[count++] = { tx, ty };
            tx -= dx[d];
            ty -= dy[d];
        }

        // 4개 이상 연속되면 승리 연출 시작!
        if (count >= 4) {
            // 3번 깜빡이는 연출 (▣ -> ■ -> ▣ -> ■ -> ▣ -> ■)
            for (int loop = 0; loop < 3; loop++) {
                // ■ 모양으로 변경 후 출력
                for (int s = 0; s < count; s++) {
                    board[win_stones[s].first][win_stones[s].second] = "■";
                }
                Console_update();
                wait;

                // 원래 돌 모양(now_pl)으로 복구 후 출력 (마지막 루프 제외)
                if (loop < 2) {
                    for (int s = 0; s < count; s++) {
                        board[win_stones[s].first][win_stones[s].second] = now_pl;
                    }
                    Console_update();
                    wait;
                }
            }

            cout << now_pl << " WIN!!\n";
            cout << (now_pl == "O" ? "X" : "O") << " LOSE\n";

            return true;
        }
    }
    return false;
}


int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    ////////////
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    First_set();
    int x;
    for (;;) {
        int i;

        now_pl = "O";
        cin >> x;
        i = Make_move(x);
        if (Win_ck(x, i)) {
            break;
        }

        now_pl = "X";
        cin >> x;
        i = Make_move(x);
        if (Win_ck(x, i)) {
            break;
        }
    }
    ////////////
    return 0;
}
