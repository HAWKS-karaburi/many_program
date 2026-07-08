#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <windows.h>
#include <Lmcons.h>
#include <intrin.h>
#include <dxgi.h> 

using namespace std;

struct SystemInfo {
    string user;
    string computer;
    string os;
    string cpu;
    string gpu;
    string ram;
    string disk;
    string uptime;
};

// 앞뒤 공백을 제거하는 헬퍼 함수
string Trim(const string& str) {
    size_t first = str.find_first_not_of(" \t\r\n");
    if (first == string::npos) return "";
    size_t last = str.find_last_not_of(" \t\r\n");
    return str.substr(first, (last - first + 1));
}

// GPU 이름 가져오기 (DXGI API 활용)
string GetGPUName() {
    IDXGIFactory* pFactory = nullptr;
    if (FAILED(CreateDXGIFactory(__uuidof(IDXGIFactory), (void**)&pFactory))) {
        return "Unknown GPU";
    }

    IDXGIAdapter* pAdapter = nullptr;
    if (pFactory->EnumAdapters(0, &pAdapter) != DXGI_ERROR_NOT_FOUND) {
        DXGI_ADAPTER_DESC desc;
        pAdapter->GetDesc(&desc);
        
        // WCHAR(기본 문자열)를 string으로 변환
        char ch[128];
        char def = ' ';
        WideCharToMultiByte(CP_ACP, 0, desc.Description, -1, ch, 128, &def, NULL);
        
        pAdapter->Release();
        pFactory->Release();
        return Trim(string(ch));
    }

    pFactory->Release();
    return "Unknown GPU";
}

// 디스크 공간 정보 가져오기 (C드라이브 기준)
string GetDiskSpace() {
    ULARGE_INTEGER freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;
    if (GetDiskFreeSpaceExA("C:\\", &freeBytesAvailable, &totalNumberOfBytes, &totalNumberOfFreeBytes)) {
        double totalGB = totalNumberOfBytes.QuadPart / 1024.0 / 1024 / 1024;
        double freeGB = totalNumberOfFreeBytes.QuadPart / 1024.0 / 1024 / 1024;
        double usedGB = totalGB - freeGB;

        stringstream ss;
        ss << fixed << setprecision(1) << usedGB << " / " << totalGB << " GB (" 
           << fixed << setprecision(0) << (freeGB / totalGB * 100) << "% free)";
        return ss.str();
    }
    return "Unknown Disk";
}

SystemInfo GetSystemInfo() {
    SystemInfo info;

    // 1. User & Computer Name
    char user[UNLEN + 1];
    DWORD len = UNLEN + 1;
    GetUserNameA(user, &len);
    info.user = user;

    char pc[MAX_COMPUTERNAME_LENGTH + 1];
    len = MAX_COMPUTERNAME_LENGTH + 1;
    GetComputerNameA(pc, &len);
    info.computer = pc;

    // 2. OS Name
    info.os = "Windows 11 (64-bit)";

    // 3. CPU Name
    int cpuInfo[4];
    char brand[64]{};
    __cpuid(cpuInfo, 0x80000002); memcpy(brand, cpuInfo, sizeof(cpuInfo));
    __cpuid(cpuInfo, 0x80000003); memcpy(brand + 16, cpuInfo, sizeof(cpuInfo));
    __cpuid(cpuInfo, 0x80000004); memcpy(brand + 32, cpuInfo, sizeof(cpuInfo));
    info.cpu = Trim(string(brand));

    // 4. GPU Name
    info.gpu = GetGPUName();

    // 5. RAM Usage
    MEMORYSTATUSEX mem{};
    mem.dwLength = sizeof(mem);
    GlobalMemoryStatusEx(&mem);
    double total = mem.ullTotalPhys / 1024.0 / 1024 / 1024;
    double used = (mem.ullTotalPhys - mem.ullAvailPhys) / 1024.0 / 1024 / 1024;
    stringstream ss;
    ss << fixed << setprecision(1) << used << " / " << total << " GB";
    info.ram = ss.str();

    // 6. Disk Space
    info.disk = GetDiskSpace();

    // 7. Uptime (빠른 시작 켜기 세션을 무시한 실제 운영체제 부팅 시간 기준 계산)
    typedef NTSTATUS(WINAPI* PFN_NtQuerySystemInformation)(int, PVOID, ULONG, PULONG);
    PFN_NtQuerySystemInformation NtQuerySystemInformation = 
        (PFN_NtQuerySystemInformation)GetProcAddress(GetModuleHandleA("ntdll.dll"), "NtQuerySystemInformation");

    ULONGLONG uptime_seconds = 0;
    if (NtQuerySystemInformation != nullptr) {
        struct MY_SYSTEM_TIMEOFDAY_INFORMATION {
            LARGE_INTEGER BootTime;
            LARGE_INTEGER CurrentTime;
            LARGE_INTEGER TimeZoneBias;
            ULONG TimeZoneId;
            ULONG Reserved;
            ULONGLONG BootTimeBias;
            ULONGLONG SleepTimeBias;
        } toad;

        // SYSTEM_INFORMATION_CLASS 3번은 SystemTimeOfDayInformation 입니다.
        if (NtQuerySystemInformation(3, &toad, sizeof(toad), nullptr) == 0) {
            LONGLONG uptime_100ns = toad.CurrentTime.QuadPart - toad.BootTime.QuadPart - toad.SleepTimeBias;
            uptime_seconds = uptime_100ns / 10000000; 
        }
    }

    // NtQuery 실패 시 백업용으로 기존 GetTickCount64 사용
    if (uptime_seconds == 0) {
        uptime_seconds = GetTickCount64() / 1000;
    }

    int h = uptime_seconds / 3600;
    int m = (uptime_seconds % 3600) / 60;
    info.uptime = to_string(h) + "h " + to_string(m) + "m";

    return info;
}

int main() {
    // UTF-8 및 ANSI 이스케이프 시퀀스 활성화
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
    
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD dwMode = 0;
    GetConsoleMode(hOut, &dwMode);
    SetConsoleMode(hOut, dwMode | ENABLE_VIRTUAL_TERMINAL_PROCESSING);

    SystemInfo info = GetSystemInfo();

    // 윈도우 로고 아스키아트 (줄 맞춤 가독성을 위해 단색 문자 구성)
    vector<string> logo = {
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "                              ",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████",
        "██████████████  ██████████████"
    };

    // 로고 행별 그라데이션 색상 (짙은 파랑 -> 밝은 하늘색)
    vector<string> logo_colors = {
        "\033[38;5;26m",  
        "\033[38;5;27m",  
        "\033[38;5;32m",  
        "\033[38;5;33m",  
        "\033[38;5;38m",  
        "\033[38;5;39m",  
        "\033[0m",         // 빈 줄 색상 초기화
        "\033[38;5;44m",  
        "\033[38;5;45m",  
        "\033[38;5;51m",  
        "\033[38;5;81m",  
        "\033[38;5;117m", 
        "\033[38;5;123m"  
    };

    vector<pair<string, string>> data = {
        {"User", info.user + "@" + info.computer},
        {"OS", info.os},
        {"CPU", info.cpu},
        {"GPU", info.gpu},
        {"RAM", info.ram},
        {"Disk", info.disk},
        {"Uptime", info.uptime},
    };

    size_t rows = max(logo.size(), data.size());
    const size_t logo_width = 34; // 화면상의 눈에 보이는 가상의 로고 너비

    for (size_t i = 0; i < rows; i++) {
        // 1. 그라데이션 로고 출력
        if (i < logo.size()) {
            cout << logo_colors[i] << logo[i] << "    ";
        } else {
            cout << string(logo_width + 4, ' ');
        }

        // 2. 시스템 정보 텍스트 출력
        if (i < data.size()) {
            cout << "\033[92m" << left << setw(8) << data[i].first 
                 << "\033[0m: " << data[i].second;
        }

        cout << '\n';
    }

    // 콘솔 색상 원래대로 복구
    cout << "\033[0m"; 
    system("pause");
    return 0;
}