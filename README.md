# 술믈리愛 (Sulmuliae)

**술믈리愛**는 전 세계 다양한 술과 음주 문화를 사랑하는 사람들을 위한 커뮤니티 플랫폼입니다. 이 플랫폼을 통해 사용자들은 술에 대한 정보 공유, 리뷰 및 평가, 추천 주류 탐색, 그리고 깊이 있는 대화를 나눌 수 있습니다. 또한 각자의 취향에 맞는 술을 발견하고, 애주가들과 소통하며 자신만의 음주 경험을 확장해 나갈 수 있는 공간을 제공합니다.

## 📜 프로젝트 개요

- **프로젝트명**: 술믈리愛
- **내용**: 술믈리愛는 전 세계 다양한 술과 음주 문화를 사랑하는 사람들을 위한 커뮤니티 플랫폼 입니다. 술에 대한 정보 공유, 리뷰 및 평가, 추천 주류 탐색, 그리고 술에 대한 깊이 있는 대화를 나눌 수 있습니다.사용자들은 각자의 취향에 맞는 술을 발견하고, 애주가들과 소통하며 자신만의 음주 경험을 확장해 나갈 수 있습니다. 술믈리愛는 술을 단순한 음료가 아닌, 문화와 예술로서 탐구하는 공간을 제공하고자 합니다.

- **프로젝트 일정**:
    - **24.09.23 ~ 24.09.26**: 기획 및 의사결정
    - **24.09.26 ~ 24.10.01**: MVP 코드 작성
    - **24.10.02 ~ 24.10.14**: 배포 및 추가 기능 코드 작성
    - **24.10.15 ~ 24.10.23**: 디버깅, 유저 테스트, 코드 리팩토링

- **주요 기능**:
    - 회원 가입 및 로그인 기능
    - 주류 평가 기능 (AI를 이용한 리뷰 요약 포함)
    - 커뮤니티 게시판 (질문 게시판, 자유 게시판, 추천 게시판)
    - 실시간 채팅 기능 (술친구 채팅방)
    - AI 기반 술 추천 챗봇
    - 이달의 술 판매 및 결제 기능

## 📜 ERDiagram

![image](https://github.com/user-attachments/assets/a783a808-ff8b-4859-9ace-110222fc0ea4)

## 📜 Process Flow

- **기본 기능**
![image](https://github.com/user-attachments/assets/4430a14f-9417-4263-8f1c-e2e6c4b6f6f0)

- **추가 기능**
    - 술친구실시간채팅
      
      ![image](https://github.com/user-attachments/assets/cd125e15-1a35-4086-9fe1-98f2ab0dab84)
      
    - 술추천챗봇
      
      ![image](https://github.com/user-attachments/assets/b34733fc-a8b5-4d93-b6d7-04e04af340ba)
      
    - 이달의 술 판매
      
      ![image](https://github.com/user-attachments/assets/22e7500f-e556-46b8-a4f9-d3c5de5b2510)
      
    - 리뷰 요약
      
      ![image](https://github.com/user-attachments/assets/66f71a7b-ae93-4392-8d75-8aeb32a23599)
      
    - 팔로우/팔로잉
      
      ![image](https://github.com/user-attachments/assets/41018286-e2ec-4b75-becf-eb04acb463c5)
      
    - 블라인드
      
      ![image](https://github.com/user-attachments/assets/ac04560f-0183-4a57-8b49-dbc0c0f8ea16)


## 💭 기술적 의사결정

- **Docker를 사용한 이유**

  Docker는 환경 일관성을 유지하고 종속성 격리 및 관리가 가능하며, CI/CD 통합을 통해 빠르고 효율적인 배포를 지원합니다. 또한, 경량화된 컨테이너를 활용하여 확장성과 자원 효율성을 높일 수 있어, 마이크로서비스 아키텍처에 적합합니다. 개발, 테스트, 배포의 전 과정에서 안정성과 유연성을 제공하기 때문에 Docker를 사용하게 되었습니다.

- **PostgreSQL을 사용한 이유**

  PostgreSQL은 MySQL보다 Django와의 호환성이 뛰어나며 더 풍부한 데이터 타입과 고급 쿼리 기능을 지원해 유용합니다. 데이터 무결성을 더 잘 보장하며, 확장성 면에서도 다양한 확장 기능을 제공합니다. 이러한 이유로 PostgreSQL을 데이터베이스 관리 시스템(RDBMS)으로 선택했습니다.

- **Django Admin Page(Back Office)를 사용한 이유**

  저희 서비스에서 주류 평가 게시, 수정, 삭제 등과 AI로 요약한 리뷰는 사용자 페이지에 표시될 필요가 없습니다. 관리의 용이성을 위해 백오피스(Back Office)를 구축하기로 하였으며, Django Admin을 사용하여 관리 인터페이스를 제공합니다. 별도의 코드 작성 없이 데이터를 쉽게 관리할 수 있어 개발 기간이 짧은 프로젝트에 적합하며, 커스터마이징을 통해 각 프로젝트에 맞는 관리 도구를 구축할 수 있어 효율적인 데이터 관리와 운영 지원을 위해 Django Admin을 선택했습니다.

- **GOOGLE SMTP을 사용한 이유**

  구글 SMTP는 높은 안정성과 강력한 보안 프로토콜을 제공하며, 별도의 SMTP 서버 설정 없이 Google 계정을 통해 쉽게 이메일을 전송할 수 있기 때문에 이메일 인증 기술로 선택하였습니다.

- **DeepL을 이용한 번역의 이유**

  AI 기반 챗봇과 리뷰 요약 기능의 유지비를 절감하기 위해, DeepL API를 사용하여 번역을 처리했습니다. GPT-4의 경우 한글은 영어보다 4배 많은 토큰을 소모하므로, 번역을 DeepL API로 처리함으로써 서비스를 더 경제적으로 운영할 수 있다고 판단했습니다.

- **AI 요약 기능**

  AI 요약 기능 구현에는 두 가지 방법을 시도해 보았고, 최종적으로 View에 직접 AI 요약 기능을 구현하기로 결정했습니다. AI 봇을 별도의 앱으로 구현하는 방식에 비해 코드가 단순하고 직관적이어서 유지보수가 용이하다고 판단하였습니다. 또한, 이 기능에 대한 확장 계획이 없으므로 확장성보다는 편리성에 중점을 두어 선택했습니다.


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

## 📦 기술 문서

- [API 명세](https://www.notion.so/fff2dc3ef51481afabb9c8484b5e0fa4?pvs=21)
- [트러블 슈팅](https://www.notion.so/f294f4a8c28243aab3860bf7bb2e929e?pvs=21)
- [코드 리팩토링](https://www.notion.so/6b9bcc4c6e4d4fb0b004dffd9810e071?pvs=21)

