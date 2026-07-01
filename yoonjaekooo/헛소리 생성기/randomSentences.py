#
# Used Gemini-3-Flash + Claude Sonnet 4.6
# Owner: yoonjaekooo
# 헛소리 생성기 (뇌절 강화판)
#

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Literal


@dataclass
class WordPack:
    adjectives: list[str] = field(default_factory=list)
    nouns: list[str] = field(default_factory=list)
    verbs: list[str] = field(default_factory=list)
    daily_terms: list[str] = field(default_factory=list)
    tech_terms: list[str] = field(default_factory=list)
    startup_terms: list[str] = field(default_factory=list)
    government_terms: list[str] = field(default_factory=list)
    company_terms: list[str] = field(default_factory=list)
    buzz_english: list[str] = field(default_factory=list)
    acronyms: list[str] = field(default_factory=list)
    closing_phrases: list[str] = field(default_factory=list)


class BrainDeadGenerator:
    def __init__(self) -> None:
        self.word_pack = self._build_word_pack()
        self.templates = self._build_templates()
        self.prefixes = [
            "차세대", "분산형", "AI 기반", "지능형", "자율형", "연계형", "통합형", "실시간",
            "클라우드 기반", "디지털 트윈 기반", "초연결", "블록체인 기반", "멀티레벨", "하이브리드",
            "오토메이티드", "메타버스형", "스마트", "네트워크형", "의사결정형", "지능화된",
            # --- 뇌절 강화: 추가 접두사 ---
            "초협력적", "양자내성", "탄소중립형", "ESG연계형", "넷제로", "온디바이스",
            "프라이버시바이디자인", "제로트러스트", "풀스택", "엔드투엔드", "데이터드리븐",
            "휴먼인더루프", "버티컬형", "호라이즌형", "리얼타임 임팩트형", "초개인맞춤형",
            "탈중앙화", "엣지네이티브", "옵저버빌리티 강화", "셀프힐링형"
        ]
        self.random = random.Random()

    def _build_word_pack(self) -> WordPack:
        pack = WordPack()
        pack.adjectives = self._generate_words(
            [
                "차세대", "분산형", "지능형", "자율형", "디지털", "실시간", "통합형", "융합형",
                "확장형", "고도화된", "자동화된", "모듈형", "스마트", "유연한", "지속가능한",
                "예측형", "최적화된", "연계형", "친환경적", "가속형", "상호작용형", "생태계형",
                "시맨틱", "네트워크형", "상시적", "초고속", "정밀한", "대규모", "비대칭", "복합적", "다층적",
                "다중형", "무선형", "위치기반", "개인맞춤", "직관형", "실증형", "초개인화", "오프라인", "온라인", "지속형",
                "사전예측", "대화형", "미래지향", "로컬형", "글로벌형", "연속형", "균형형", "동적형", "상향형", "하향형",
                "공익형", "민간형", "공공형", "연합형", "복원형", "표준형", "로봇형", "환경친화", "재사용형", "합성형"
            ],
            ["형", "성", "적", "화", "기반", "구조", "인프라", "솔루션", "프레임워크", "플랫폼", "엔진", "모델", "네트워크", "시스템", "로직", "아키텍처", "기술"],
        )
        pack.nouns = self._generate_words(
            [
                "감자", "고양이", "배터리", "프로토콜", "모듈", "센서", "리소스", "데이터", "노드",
                "코어", "리스크", "플로우", "시너지", "오퍼레이션", "클러스터", "인사이트", "논리",
                "시뮬레이션", "토폴로지", "큐레이션", "상상력", "온톨로지", "스택", "카탈로그",
                "메트릭", "워크로드", "도메인", "가치", "통합체", "인프라", "이력서", "시그널", "메커니즘",
                "로직", "매트릭스", "미러", "반복기", "패턴", "트리거", "지표", "콘텐츠", "인구", "에코",
                "피드백", "서킷", "버퍼", "이벤트", "프레임", "커넥터", "오토마타", "루프백", "테마", "정책",
                "모니터", "분석기", "대시보드", "트랜잭션", "리모컨", "볼트", "트랜스폼", "레벨업", "세그먼트", "리포트"
            ],
            ["화", "성", "체", "축", "망", "센터", "포인트", "공간", "레벨", "인프라", "노드", "라이프", "스코프", "파라미터", "필터", "스토리지", "리포지토리"],
        )
        pack.verbs = self._generate_words(
            [
                "개선한다", "연결한다", "최적화한다", "자동화한다", "통합한다", "재구성한다",
                "가속화한다", "확장한다", "분석한다", "활성화한다", "모니터링한다", "개발한다",
                "공유한다", "협업한다", "정렬한다", "설계한다", "구현한다", "파악한다", "재배치한다",
                "검증한다", "조율한다", "확립한다", "생성한다", "도입한다", "운영한다", "재정의한다",
                "실현한다", "민감화한다", "보강한다", "시뮬레이션한다", "우선화한다", "격상한다", "재활용한다",
                "가중한다", "정규화한다", "구분한다", "심화한다", "완성한다", "평가한다", "전환한다",
                "표준화한다", "예측한다", "반영한다", "지속한다", "조정한다", "개편한다", "증강한다",
                "보완한다", "재정렬한다", "다중화한다", "매핑한다", "포켓화한다", "시각화한다", "네트워크화한다"
            ],
            ["화", "성", "력", "처리", "연계", "모드", "레이어", "프로세스", "캠페인", "모델", "디자인", "기반", "분석", "관리", "개발", "엔진"],
        )
        pack.daily_terms = self._generate_words(
            [
                "치킨", "바나나", "똥", "커피", "라면", "떡볶이", "김밥", "피자", "맥주", "햄버거",
                "아이스크림", "김치", "우유", "빵", "고구마", "호박", "마늘", "양파", "사과", "배추",
                "오징어", "꽈배기", "삼겹살", "파전", "순대", "비빔밥", "국밥", "짬뽕", "우동", "냉면",
                "도넛", "젤리", "초콜릿", "김말이", "튀김", "닭갈비", "쌀국수", "곱창", "타코", "샌드위치",
                "샐러드", "핫도그", "카레", "돈까스", "초밥", "냉모밀", "오므라이스", "떡국", "순두부", "족발",
                "감자칩", "과자", "복숭아", "포도", "수박", "멜론", "참치", "오이", "토마토", "오렌지"
            ],
            ["팩", "박스", "칩", "볼", "통", "덩어리", "세트", "봉지", "포장", "상자", "조각", "모음", "한입", "리미트", "라인", "로드", "플랜", "클럽", "코너", "에디션"],
        )
        pack.tech_terms = self._generate_words(
            [
                "로봇", "네트워크", "알고리즘", "인공지능", "클라우드", "시스템", "데이터베이스", "머신러닝",
                "딥러닝", "컴퓨팅", "분산처리", "가상화", "모듈러", "컨테이너", "오케스트레이션",
                "파이프라인", "프레임워크", "API", "SDK", "엔진", "파라미터", "시뮬레이터", "서보",
                "임베디드", "메모리", "프로토콜", "코어", "플랫폼", "서버", "클라이언트", "분석엔진",
                "블록체인", "메타데이터", "캐시", "쿼리", "트랜스포머", "벡터", "그래프", "토큰", "모델서빙",
                "에지컴퓨팅", "하이브리드클라우드", "솔루션엔진", "분산스토리지", "데이터파이프", "객체스토리지",
                "오토스케일링", "패턴매칭", "시맨틱검색", "데이터레이크", "에이전트", "마이크로서비스", "클라우드네이티브"
            ],
            ["엔진", "서버", "모듈", "스택", "랩", "클러스터", "프레임", "코어", "네트워크", "API", "SDK", "플랫폼", "오브젝트", "러너", "서비스", "파이프", "레이어"],
        )
        pack.startup_terms = self._generate_words(
            [
                "디스커버리", "스케일업", "엑셀러레이터", "피벗", "MVP", "코호트", "퍼널", "CRO",
                "고객여정", "플랫폼", "시드", "런칭", "유저", "세일즈", "마케팅", "브랜딩", "커뮤니티",
                "리텐션", "리드", "프로덕트", "모멘텀", "네트워크", "옵티마이즈", "레버리지", "스테이크",
                "알파", "베타", "패널", "디자인씽킹", "리서치", "트렌드", "성장엔진", "디지털고객", "캠페인",
                "네오", "프로토타입", "엔젤", "지분", "투자유치", "얼라이언스", "파트너십", "앵커", "온보딩",
                "잭팟", "프리세일", "서비스디자인", "사용자경험", "프로덕트마켓핏", "기여도", "가입유도", "리워드",
                "성장실험", "사용자분석", "고객세그먼트", "채널전략", "오퍼레이션", "실험군", "컨트롤군", "아웃라이어"
            ],
            ["랩", "클럽", "네트워크", "오큘러스", "코어", "포인트", "파이프", "허브", "플랫폼", "스페이스", "센터", "플로우", "스토리", "모델", "엔진", "에코시스템"],
        )
        pack.government_terms = self._generate_words(
            [
                "국가", "과제", "기획", "전략", "연구개발", "융합", "기술개발", "자원활용", "사회문제",
                "공공데이터", "정책연계", "산업화", "확산", "기반조성", "신산업", "기술혁신", "고도화",
                "분야간", "협력체계", "정책지원", "공공서비스", "혁신성장", "사업화", "위탁연구",
                "전략기획", "실증연구", "실용화", "정책연구", "협업체계", "예비타당성", "제도개선",
                "기술이전", "국정과제", "수요분석", "공공연계", "사회문제해결", "데이터기반정책", "기술수요조사",
                "지능형행정", "공공혁신", "정책실험", "사회적가치", "공공투자", "지역상생", "산학협력",
                "연구성과", "실증사업", "지역산업", "재난대응", "글로벌협력", "과학기술정책", "기술확산"
            ],
            ["사업", "프로그램", "체계", "정책", "플랫폼", "개발", "지원", "연계", "구축", "분석", "모델", "로드맵", "지원체계", "협력체계", "위원회", "심의"],
        )
        pack.company_terms = self._generate_words(
            [
                "효율화", "성과관리", "리스크관리", "거버넌스", "전략보고", "경영진단", "브랜드",
                "조직개편", "사업포트폴리오", "지식재산", "생산성", "품질관리", "프로세스개선",
                "프로젝트포트폴리오", "인사전략", "시너지창출", "사업전략", "수익모델", "고객가치",
                "운영체계", "통합관리", "재무구조", "마케팅전략", "수요예측", "스탠다드", "제안서",
                "협업체계", "리더십", "프로그램관리", "서비스품질", "투자심사", "경영계획", "인사평가",
                "경영전략", "조직문화", "리더십개발", "예산관리", "공정성", "고객만족", "대외협력", "부문별성과",
                "데이터거버넌스", "전략수립", "사업계획", "업무표준", "가치사슬", "미션전략", "운영리스크", "윤리경영"
            ],
            ["보고서", "전략", "지표", "개선", "분석", "모델", "대시보드", "운영", "기준", "체계", "포인트", "정책", "시스템", "프로세스", "플랫폼", "워크플로우"],
        )
        # --- 뇌절 강화: 신규 카테고리 ---
        pack.buzz_english = [
            "synergy", "leverage", "paradigm shift", "disruption", "scalability",
            "deep dive", "low-hanging fruit", "north star metric", "win-win",
            "bandwidth", "circle back", "move the needle", "value proposition",
            "best practice", "actionable insight", "ecosystem play", "growth hacking",
            "blue ocean", "first mover advantage", "bleeding edge", "agile mindset",
            "thought leadership", "core competency", "game changer", "holistic approach",
        ]
        pack.acronyms = [
            "KPI", "OKR", "ROI", "TF", "PoC", "MVP", "SLA", "TCO", "B2B", "B2C",
            "API", "SDK", "CRM", "ERP", "QA", "R&D", "CTO", "CSO", "DAU", "MAU",
            "NPS", "CAC", "LTV", "MOU", "RFP",
        ]
        pack.closing_phrases = [
            "를 위한 TF를 즉시 구성한다",
            "에 대한 로드맵을 차질없이 수립한다",
            "의 거버넌스 체계를 전사적으로 정립한다",
            "을 위한 협의체를 신속히 발족한다",
            "에 대한 추진단을 한시적으로 운영한다",
            "의 성과지표를 분기별로 재점검한다",
            "을 위한 파일럿을 선제적으로 추진한다",
            "에 대한 컨센서스를 전방위적으로 형성한다",
            "의 액션플랜을 수립하고 즉시 실행한다",
            "을 위한 워킹그룹을 상시 가동한다",
        ]
        return pack

    def _generate_words(self, stems: list[str], endings: list[str], min_count: int = 100) -> list[str]:
        words: list[str] = []
        seen: set[str] = set()
        for stem in stems:
            for ending in endings:
                combo = f"{stem}{ending}"
                if combo not in seen:
                    seen.add(combo)
                    words.append(combo)
        for stem in stems:
            if stem not in seen:
                seen.add(stem)
                words.append(stem)
        while len(words) < min_count:
            for stem in stems:
                if len(words) >= min_count:
                    break
                token = f"{stem}{self.random.choice(endings)}"
                if token not in seen:
                    seen.add(token)
                    words.append(token)
        return words

    def _build_templates(self) -> list[str]:
        return [
            "{형용사} {명사} 플랫폼",
            "{기술용어} 기반 {형용사} {명사} 시스템",
            "{명사} 중심 {형용사} 생태계 구축",
            "AI 기반 {명사}의 {형용사} {명사} 자동화 기술 개발",
            "{형용사} {명사} 최적화를 위한 {기술용어} 프레임워크",
            "{스타트업용어} 기반 {명사} {동사} 솔루션",
            "{정부과제용어} 연계 {형용사} {명사} 연구개발",
            "{기업용어} 중심 {형용사} {명사} 운영 체계",
            "{일상용어}와 {기술용어}를 활용한 {형용사} {명사} 전략",
            "{형용사} {명사}와 {명사}의 {기술용어} 융합",
            "{동사} 가능한 {형용사} {명사} 인프라",
            "{명사}와 {명사}를 연결하는 {형용사} {기술용어} 네트워크",
            "{형용사} {명사} 자동화를 위한 {스타트업용어} 기반 {기술용어}",
            "{기술용어}와 {기업용어}로 구현하는 {형용사} {명사} 구조",
            "{정부과제용어}와 {기업용어}를 통합한 {형용사} {명사} 로드맵",
            "{일상용어}를 중심으로 한 {형용사} {명사} 인터페이스",
            "{형용사} {명사} 생성과 {명사} 최적화를 위한 {기술용어} 프로세스",
            "{스타트업용어} 중심 {기술용어} 및 {기업용어} 통합 플랫폼",
            "{명사} 기반 {형용사} {명사} 운영 모델",
            "{형용사} {명사} 디지털 트윈과 {기술용어} 융합",
            "{정부과제용어} 기반 {형용사} {명사} 실증 연구",
            "{기업용어}로 구현된 {형용사} {명사} 혁신 체계",
            "{동사} 가능한 {형용사} {명사} 솔루션 프레임워크",
            "{일상용어}와 {명사}를 연결하는 {기술용어} 기반 {형용사} 전략",
            "{형용사} {명사} 확장을 위한 {스타트업용어} 중심 {기술용어}",
            "{기술용어}와 {일상용어}의 {형용사} 상호작용 메커니즘",
            "{명사} 중심 {기업용어} 및 {정부과제용어} 융합 모델",
            "{형용사} {명사} 가속화를 위한 {기업용어} 오케스트레이션",
            "{명사}와 {명사}의 {형용사} 연결을 위한 {기술용어} 레이어",
            "{스타트업용어} 기반 {형용사} {명사} 생태계 촉진",
            "{정부과제용어} 지원 {형용사} {명사} 사업화 전략",
            "{기업용어} 관점의 {형용사} {명사} 데이터 관리",
            "{동사} 가능한 {명사} 중심 {형용사} 프로토콜",
            "{형용사} {명사} 경험을 위한 {일상용어} 기반 {기술용어}",
            "{기업용어}와 {정부과제용어}를 결합한 {형용사} {명사} 추진체계",
            "{스타트업용어}로 구현된 {형용사} {명사} 가치 생성",
            "{기술용어} 기반 {형용사} {명사} 자원 최적화",
            "{명사}와 {기술용어}의 {형용사} 시너지 창출",
            "{기업용어} 중심 {명사} 통합 및 {형용사} 운영 혁신",
            "{동사} 가능 {형용사} {명사} 시스템 설계",
            "{형용사} {기술용어} 패러다임과 {명사} 자동화",
            "{정부과제용어} 연계 {스타트업용어}와 {기업용어} 융합",
            "{명사} 우선 {형용사} {기술용어} 인큐베이션",
            "{일상용어}를 활용한 {형용사} {명사} 피드백 루프",
            "{형용사} {명사} 성과를 위한 {기술용어} 기반 서킷",
            "{기업용어}와 {정부과제용어}의 {형용사} {명사} 실무체계",
            "{스타트업용어}와 {일상용어}를 결합한 {형용사} {명사} 모델",
            "{형용사} {명사} 확장과 {기술용어} 통합 자동화",
            "{명사} 기반 {기업용어} 정렬과 {형용사} {명사} 최적화",
            "{정부과제용어} 실증을 위한 {형용사} {명사} 디지털 플랫폼",
            "{형용사} {명사} 실현을 위한 {기술용어} 혁신 로드맵",
            "{스타트업용어} 중심 {기업용어}와 {기술용어}의 {형용사} 프로토콜",
            "{형용사} {명사} 융합과 {기술용어} 확산의 {명사} 메커니즘",
            "{일상용어} 연계 {기술용어} 기반 {형용사} {명사} 에코시스템",
            "{기업용어} 관점의 {형용사} {명사} 레버리지 구조",
            "{정부과제용어}와 {스타트업용어}를 결합한 {형용사} {명사} 전략",
            "{형용사} {명사} 운영을 위한 {기술용어} 및 {기업용어} 프레임워크",
            # --- 뇌절 강화: 영어 버즈워드 / 약자 / 순환논리 / 종결구 템플릿 ---
            "{영어버즈} 관점에서 본 {형용사} {명사}의 {기술용어} 전략",
            "{약자} 기반 {형용사} {명사} {약자} 달성 체계",
            "{영어버즈}를 {동사} {형용사} {기업용어} {명사}",
            "본 {명사}는 본 {명사}의 {형용사} 목적을 달성하기 위해 {기술용어}를 {동사}",
            "{형용사} {명사}{종결구}",
            "{기업용어}와 {정부과제용어}의 {영어버즈}를 통한 {형용사} {명사}{종결구}",
            "{스타트업용어} 기반 {약자} 향상을 위한 {형용사} {기술용어} {영어버즈}",
            "{명사}의 {형용사} {명사}화는 {명사}의 {형용사} {명사}화를 전제로 {동사}",
            "{기술용어} {영어버즈} 기반 {약자}/{약자} 동시 개선 {명사}",
            "{형용사} {명사} {영어버즈}를 위한 {기업용어} {종결구}",
        ]

    def _pick_word(self, category: str) -> str:
        mapping = {
            "형용사": self.word_pack.adjectives,
            "명사": self.word_pack.nouns,
            "동사": self.word_pack.verbs,
            "일상용어": self.word_pack.daily_terms,
            "기술용어": self.word_pack.tech_terms,
            "스타트업용어": self.word_pack.startup_terms,
            "정부과제용어": self.word_pack.government_terms,
            "기업용어": self.word_pack.company_terms,
            "영어버즈": self.word_pack.buzz_english,
            "약자": self.word_pack.acronyms,
            "종결구": self.word_pack.closing_phrases,
        }
        return self.random.choice(mapping[category])

    def _expand_phrase(self, phrase: str, brain_level: int, depth: int = 0) -> str:
        if depth >= 3:
            return phrase
        threshold = 0.20 + min(brain_level, 120) / 1000.0
        if self.random.random() < threshold:
            prefix = self.random.choice(self.prefixes)
            expanded = f"{prefix} {phrase}"
            if depth < 2 and self.random.random() < 0.6:
                return self._expand_phrase(expanded, brain_level, depth + 1)
            return expanded
        return phrase

    def _maybe_inject_buzzword(self, text: str, brain_level: int) -> str:
        """뇌절 강화: 뇌절 레벨이 높을수록 영어 버즈워드/약자를 한글 단어 경계에 자연스럽게 삽입.
        (영단어 토큰 자체를 쪼개지 않도록 순수 한글 토큰 뒤에만 붙인다.)"""
        inject_chance = min(brain_level, 150) / 300.0
        if self.random.random() < inject_chance:
            buzz = self.random.choice(self.word_pack.buzz_english + self.word_pack.acronyms)
            words = text.split(" ")
            candidates = [i for i, w in enumerate(words) if w.isascii() is False and "(" not in w]
            if candidates:
                insert_at = self.random.choice(candidates)
                words.insert(insert_at + 1, f"({buzz})")
                return " ".join(words)
        return text

    def _fill_template(self, template: str, brain_level: int) -> str:
        values = {
            "형용사": self._expand_phrase(self._pick_word("형용사"), brain_level),
            "명사": self._expand_phrase(self._pick_word("명사"), brain_level),
            "동사": self._expand_phrase(self._pick_word("동사"), brain_level),
            "일상용어": self._expand_phrase(self._pick_word("일상용어"), brain_level),
            "기술용어": self._expand_phrase(self._pick_word("기술용어"), brain_level),
            "스타트업용어": self._expand_phrase(self._pick_word("스타트업용어"), brain_level),
            "정부과제용어": self._expand_phrase(self._pick_word("정부과제용어"), brain_level),
            "기업용어": self._expand_phrase(self._pick_word("기업용어"), brain_level),
            # --- 뇌절 강화: 신규 카테고리 값 ---
            "영어버즈": self._pick_word("영어버즈"),
            "약자": self._pick_word("약자"),
            "종결구": self._pick_word("종결구"),
        }
        filled = template.format(**values)
        return self._maybe_inject_buzzword(filled, brain_level)

    def _word_count(self, text: str) -> int:
        return len(text.split())

    def generate_sentence(self, brain_level: int = 20, mode: str = "NORMAL") -> str:
        mode = mode.upper()
        if mode == "SHORT":
            target_words = 8
            segment_count = 1
        elif mode == "NORMAL":
            target_words = 12
            segment_count = 2
        elif mode == "LONG":
            target_words = 22
            segment_count = 3 + (1 if brain_level > 30 else 0)
        elif mode == "INSANE":
            target_words = 60
            segment_count = 6 + (1 if brain_level > 60 else 0)
        else:
            target_words = 12
            segment_count = 2

        if brain_level <= 10:
            target_words = max(4, target_words - 2)
        elif brain_level <= 30:
            target_words += 2
        elif brain_level <= 60:
            target_words += 4
        elif brain_level <= 100:
            target_words += 8
        else:
            target_words += 15

        segments: list[str] = []
        for _ in range(segment_count):
            segment = self._fill_template(self.random.choice(self.templates), brain_level)
            if brain_level >= 31:
                segment = f"{segment} {self._fill_template(self.random.choice(self.templates), brain_level)}"
            if brain_level >= 61:
                segment = f"{segment} {self._fill_template(self.random.choice(self.templates), brain_level)}"
            segments.append(segment)

        sentence = " ".join(segments)
        if mode == "INSANE":
            while self._word_count(sentence) < 50:
                sentence = f"{sentence} {self._fill_template(self.random.choice(self.templates), brain_level)}"
        elif self._word_count(sentence) < target_words:
            while self._word_count(sentence) < target_words:
                sentence = f"{sentence} {self._fill_template(self.random.choice(self.templates), brain_level)}"

        # --- 뇌절 강화: HYPER 모드 종결구 강제 부착 ---
        if mode == "INSANE" and brain_level >= 90 and self.random.random() < 0.7:
            sentence = f"{sentence} 결론적으로, 이는 {self._pick_word('영어버즈')} 관점에서 {self._pick_word('약자')}{self.random.choice(self.word_pack.closing_phrases)}"

        return sentence.replace("  ", " ").strip().rstrip(".") + "."

    def generate_project_name(self) -> str:
        templates = [
            "{기술용어} 기반 {형용사} {명사} 플랫폼",
            "{형용사} {명사} 최적화 플랫폼",
            "{스타트업용어} 기반 {명사} 솔루션",
            "{형용사} {명사} 디지털 플랫폼",
            "{약자} 연동 {형용사} {명사} {영어버즈} 플랫폼",
        ]
        return self._fill_template(self.random.choice(templates), 40).replace("  ", " ").strip()

    def generate_government_project(self) -> str:
        templates = [
            "{기술용어} 기반 {명사} 자원 활용을 위한 {형용사} {명사} 자동화 기술 개발",
            "{정부과제용어} 연계 {형용사} {명사} 실증 연구 개발",
            "{기업용어} 중심 {명사} 혁신을 위한 {형용사} {기술용어} 기반 정책 실험",
            "{정부과제용어}와 {약자} 지표를 연계한 {형용사} {명사} {영어버즈} 사업",
        ]
        return self._fill_template(self.random.choice(templates), 70).replace("  ", " ").strip()

    def generate_startup_pitch(self) -> str:
        templates = [
            "{형용사} {명사} 데이터 생태계를 혁신하는 {기술용어} 솔루션",
            "{스타트업용어} 기반 {명사} 플랫폼으로 {형용사} 가치를 창출하는 {기술용어}",
            "분산형 {명사} 생태계를 재구성하는 AI 기반 {기술용어} 서비스",
            "{영어버즈}를 극대화하는 {형용사} {명사} {스타트업용어} 솔루션",
        ]
        values = {
            "형용사": self._expand_phrase(self._pick_word("형용사"), 55),
            "명사": self._expand_phrase(self._pick_word("명사"), 55),
            "기술용어": self._expand_phrase(self._pick_word("기술용어"), 55),
            "스타트업용어": self._expand_phrase(self._pick_word("스타트업용어"), 55),
            "영어버즈": self._pick_word("영어버즈"),
        }
        return self.random.choice(templates).format(**values).replace("  ", " ").strip()

    def generate_hyper_brain_dead(self) -> str:
        # --- 뇌절 강화: 핵뇌절 레벨 상향 (150 -> 200) ---
        return self.generate_sentence(brain_level=200, mode="INSANE")


def main() -> None:
    generator = BrainDeadGenerator()
    print("=== 뇌절 문장 생성기 (강화판) ===")
    print("1. 프로젝트명 생성")
    print("2. 국책과제 생성")
    print("3. 스타트업 소개 생성")
    print("4. 뇌절 문장 생성")
    print("5. 핵뇌절 생성")
    choice = input("선택하세요: ").strip()

    if choice == "1":
        print(generator.generate_project_name())
    elif choice == "2":
        print(generator.generate_government_project())
    elif choice == "3":
        print(generator.generate_startup_pitch())
    elif choice == "4":
        brain_level = int(input("뇌절 레벨(1~200)을 입력하세요: ").strip() or "20")
        mode = input("모드(SHORT/NORMAL/LONG/INSANE)를 입력하세요: ").strip().upper() or "NORMAL"
        print(generator.generate_sentence(brain_level=brain_level, mode=mode))
    elif choice == "5":
        print(generator.generate_hyper_brain_dead())
    else:
        print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
