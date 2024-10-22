# 술믈리愛 (Sulmuliae)

**술믈리愛**는 전 세계 다양한 술과 음주 문화를 사랑하는 사람들을 위한 커뮤니티 플랫폼입니다. 이 플랫폼을 통해 사용자들은 술에 대한 정보 공유, 리뷰 및 평가, 추천 주류 탐색, 그리고 깊이 있는 대화를 나눌 수 있습니다. 또한 각자의 취향에 맞는 술을 발견하고, 애주가들과 소통하며 자신만의 음주 경험을 확장해 나갈 수 있는 공간을 제공합니다.

## 📜 프로젝트 개요

- **프로젝트명**: 술믈리愛
- **목표**: 술을 단순한 음료가 아닌, 문화와 예술로 탐구하는 커뮤니티 플랫폼을 제공
- **주요 기능**:
    - 회원 가입 및 로그인 기능
    - 주류 평가 기능 (AI를 이용한 리뷰 요약 포함)
    - 커뮤니티 게시판 (질문 게시판, 자유 게시판, 추천 게시판)
    - 실시간 채팅 기능 (술친구 채팅방)
    - AI 기반 술 추천 챗봇
    - 이달의 술 판매 및 결제 기능

## 💭 기술적 의사결정

- **Docker**: 환경 일관성 유지 및 종속성 격리, CI/CD 통합을 통해 빠르고 효율적인 배포 가능
- **PostgreSQL**: 풍부한 데이터 타입 및 고급 쿼리 기능 지원, 데이터 무결성 보장
- **Django Admin**: 관리 인터페이스로 데이터를 쉽게 관리할 수 있어 관리의 용이성 제공
- **Google SMTP**: 구글 서버의 높은 안정성 및 보안, 간편한 이메일 전송 가능
- **Deepl API**: 경제적 번역 서비스로 유지비 절감

## 🌐 배포 및 데이터베이스

- **배포 도구**: Docker, AWS (S3, Cloudfront, Route 53, EC2), Gunicorn, Nginx, Daphne
- **데이터베이스**: PostgreSQL
- **실시간 기능**: Redis, Django Channels

## 📂 기능 상세

- **회원 기능**
    - 회원가입, 로그인, 로그아웃
    - 유저 정보 수정 및 삭제 (비밀번호 변경, 회원 탈퇴)
    - 팔로우 및 블라인드 기능
- **평가 기능**
    - 평가 게시물 목록 및 상세 보기
    - 주류 평가 및 리뷰 기능
    - 좋아요 기능 (게시물, 리뷰)
- **커뮤니티 기능**
    - 커뮤니티 게시물 생성, 수정, 삭제
    - 댓글 작성, 수정, 삭제
    - 커뮤니티 게시물 및 댓글 좋아요 기능
- **술친구 채팅방 기능**
    - 채팅방 생성, 목록 조회, 삭제
- **AI 챗봇 기능**
    - GPT 기반 술 추천 챗봇
- **이달의 술 판매**
    - 장바구니 기능 및 결제 기능

## 🛠 사용 기술

- **Backend**: Django, DRF, PostgreSQL, Redis, Django Channels, Nginx, Daphne, Gunicorn
- **Frontend**: React, JavaScript
- **Cloud**: AWS (EC2, S3, Cloudfront, Route 53)
- **AI**: GPT (OpenAI API), Deepl API
- **DevOps**: Docker, Docker Compose, GitHub Actions, Portone (결제 시스템)

## 🔗 프로젝트 구조
├── accounts ├── chatbot ├── community ├── evaluations ├── products ├── chat ├── static ├── templates ├── manage.py └── requirements.txt

## 🗂 Git 컨벤션

1. **커밋 메시지 유형**:
    - `feat`: 새로운 기능 추가
    - `fix`: 버그 수정
    - `docs`: 문서 변경
    - `style`: 코드 포맷팅, 세미콜론 누락 등
    - `refactor`: 코드 리팩토링
    - `test`: 테스트 추가
    - `chore`: 빌드 과정, 보조 도구 변경

2. **브랜치 네이밍 규칙**:
    - `feature/{기능명}`
    - 커밋은 작은 단위로 자주 남길 것

3. **Merge 규칙**:
    - `dev` 브랜치에 우선 merge, 배포 시 `main`에 merge

## 📝 코드 컨벤션

- **Import 정리**: 표준 라이브러리, 외부 라이브러리, 로컬 모듈 순으로 그룹화
- **Formatter**: `black`을 이용해 PEP8 규칙 준수

## 🗓 프로젝트 일정

- **개발 시작**: 2024-09-23

## 📦 배포 및 API 문서

- [API 명세](https://www.notion.so/fff2dc3ef51481afabb9c8484b5e0fa4?pvs=21)
- [트러블 슈팅](https://www.notion.so/f294f4a8c28243aab3860bf7bb2e929e?pvs=21)
- [코드 리팩토링](https://www.notion.so/6b9bcc4c6e4d4fb0b004dffd9810e071?pvs=21)

