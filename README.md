
<br>

# 👀 welcome to Sulmeulliae 👀

### [ 애주가들을 위한 주류평가 커뮤니티 'Sulmeulliae' ](https://sulmeulliae.com/)

![image](https://github.com/user-attachments/assets/96649e7f-e0b7-4193-ac42-4fa259b85fd4)

<br><br>

## 👨‍👩‍👧‍👦 Our Team

| 이세준 | 서동인 | 김영빈 | 김나현 |
|:---:|:---:|:---:|:---:|
| [@gr22nsky](https://github.com/gr22snky) | [@Drills-hub](https://github.com/Drills-hub) | [@feliciathebeen](https://github.com/feliciathebeen) | [@nahyunkeem](https://github.com/nahyunkeem) |

<br>

### [💜 SA문서 몰아보기](https://www.notion.so/teamsparta/SA-a2ca1a6c05784de8856690dbe1f4e423)
### [💜 프론트엔드 깃허브 바로가기](https://github.com/gr22nsky/sulmeulliae_frontend)

<br><br>




## 프로젝트 기능

### 📊 주류평가

> * 관리자가 작성한 기본 주류 목록을 보고 회원은 주류를 평가할 수 있습니다.
> * 주류를 평가 할 때는 리뷰 형식으로 평점과 내용이 들어갈 수 있습니다.
> * 평과 별점을 추산하여 AI를 이용한 리뷰 요약이 제공됩니다.

<details>
<summary>미리보기</summary>
<div markdown="1">

![주류평가](https://github.com/user-attachments/assets/98e40e25-61f3-410e-9af8-1ae73424d2f6)

 <br>
</div>
</details>


### 📊 커뮤니티
 
> * 회원은 자유게시판에 술과 관련된 이야기들을 게시하고 다른 회원들과 소통할 수 있습니다.
> * 커뮤니티의 게시판에는 자유게시판, 질문게시판, 토론게시판이 있습니다. 

<details>
<summary>미리보기</summary>
<div markdown="1">

![커뮤니티](https://github.com/user-attachments/assets/52d57159-2ea1-4161-a5ab-26b59782f66e)

 <br>
</div>
</details>

### 🗨 WebSocket방식의 술친구 채팅방
 
> * 회원은 술친구를 구할 수 있는 실시간 채팅방을 이용할 수 있습니다.
> * 직접 채팅방을 만들 수도 있고, 이미 개설된 채팅방에 입장할 수 있습니다.

<details>
<summary>미리보기</summary>
<div markdown="1">

![채팅방](https://github.com/user-attachments/assets/88b71bfa-2669-419a-b518-511215b1b126)

 <br>
</div>
</details>

### 🗨 술추천 챗봇

> * 회원은 AI술추천 챗봇을 통해 술을 추천받을 수 있습니다.
> * 기분이나 최근에 맛있게 마신 술을 입력하여 술을 추천받을 수 있습니다.

<details>
<summary>미리보기</summary>
<div markdown="1">

![챗봇](https://github.com/user-attachments/assets/e61353b3-015c-44c1-b1f2-de7c2b82931b)

 <br>
</div>
</details>

### 👨‍💻 이달의 술 판매
 
> * 회원은 매달 지정된 이달의 술을 장바구니에 넣고 결제하여 구매할 수 있습니다.
> * 이달의 술은 매달 3개씩 회원들의 평가를 기준으로 선정됩니다.

<details>
<summary>미리보기</summary>
<div markdown="1">

![이달의 술](https://github.com/user-attachments/assets/b03349cd-2b6b-4c83-9e09-c875ddc18673)

 <br>
</div>
</details>

### 👨‍💻 회원프로필기능
 
> * 회원은 자신의 프로필을 수정하거나 비밀번호를 변경 및 회원탈퇴를 할 수 있는 프로필기능을 이용할 수 있습니다.
> * 회원프로필페이지에서 자신이 좋아요한 게시글이나 리뷰 및 댓글을 확인 할 수 있습니다.
> * 추가적으로 이달의 술에서 결제한 결제내역을 확인할 수 있습니다.

<details>
<summary>미리보기</summary>
<div markdown="1">

![프로필](https://github.com/user-attachments/assets/0a9eaac2-f2c4-49e2-8e67-1c1d62d3a1bc)

 <br>
</div>
</details>


## 적용 기술

### ◻ Docker _ BE

> Docker는 환경 일관성을 유지하고 종속성 격리 및 관리가 가능하며, CI/CD 통합을 통해 빠르고 효율적인 배포를 지원합니다. 또한, 경량화된 컨테이너를 활용하여 확장성과 자원 효율성을 높기 때문에, 마이크로서비스 아키텍처에 적합니다. 개발, 테스트, 배포의 전 과정에서 안정성과 유연성을 제공하기 때문에 사용하게 되었습니다.


### ◻ PostgreSQL _ BE

> PostgreSQL은 MySQL보다  Django와의 호환성이 뛰어나며 더 풍부한 데이터 타입과 고급 쿼리 기능을 지원해 유용합니다. 데이터 무결성을 더 잘 보장하며, 확장성 면에서도 다양한 확장 기능을 제공합니다. 이로 인해 PostgreSQL을 데이터베이스 관리 시스템(RDBMS)으로 사용했습니다.

### ◻ Django Admin Page(Back Office) _ BE

> 저희의 서비스에서 주류 평가 게시, 수정, 삭제 등과 AI로 요약한  리뷰 등은 서비스 페이지에 나와야 할 필요가 없으며, 관리의 용이성을 위해 백오피스(Back Office)가 필요하다고 느꼈습니다.         
> Django Admin을 기반으로 제공되는 관리 인터페이스로, 개발자가 별도의 코드를 작성하지 않고도 데이터를 쉽게 관리할 수 있기 때문에 저희처럼 개발 기간이 짧은 프로젝트에 더 용이하다고 느꼈고, 커스터마이징을 통해 각 프로젝트에 맞는 관리 도구를 구축할 수 있으므로 효율적인 데이터 관리와 운영 지원을 위해 사용하게 되었습니다.


### ◻ Github Actions (CI/CD) _ BE

> 자동 빌드/배포를 위하여 깃허브를 활용하여 CI/CD 를 구축했습니다.         

### ◻ Google SMTP _ BE

> 이메일 인증 기술을 구글 SMTP를 사용한 이유는 구글의 서버를 이용하기 때문에 높은 안정성과 강력한 보안 프로토콜을 사용한다는 점, 그리고 Google 계정을 사용하면 별도의 SMTP 서버를 설정할 필요 없이 쉽게 이메일을 전송할 수 있기 때문에 선택하게 되었습니다.     


### ◻ DeepL _ BE
 
> 저희는 AI를 이용한 챗봇과 리뷰 요약에서 서비스의 유지비를 줄이기 위해, DeepL을 이용해서 번역을 사용 했습니다.  저희가 사용한 Gpt4의 경우 글자 수 마다 토큰이 사용되는데 한글이 영어의 4배 정도이므로 번역만 DeepL의 api를 이용해서 사용한다면, 서비스를 유지하는데 더 경제적일 것이라는 판단이였습니다.


<br><br>


## 🚨 Trouble Shooting

#### [자세한내용](https://www.notion.so/teamsparta/f294f4a8c28243aab3860bf7bb2e929e?v=a69be81666584f2d829cda6dc7d4e254)

#### urls.py패턴순서 이슈
#### Authentication 이슈
#### 커뮤니티 글 생성 및 수정시 이미지 이슈 
#### Host 지정 오류 이슈
#### 리뷰 생성시 body에 넣을 필요가 없는 항목 수정 이슈
#### 회원가입 및 로그인시 lastlogin이 기록되지 않는 이슈
#### 댓글 수정시 삭제된 댓글이 호출되는 이슈
#### 배포과정중 docker 권한 이슈
#### 회원가입시 로그인페이지로 넘어가지 않는 이슈
#### 주류평가페이지를 열었을때 이미지가 로드되지 않는 이슈
#### docker-compose up 명령어 실행 오류 이슈
#### Route53 경로 지정 오류 이슈
#### Nginx, Gunicorn 연결 이슈
#### 주류상세페이지에서 좋아요를 반영하지 못하는 이슈
#### SSL Protocol 오류 이슈
#### Mixed Content 오류 이슈
#### https header 오류 이슈
#### 프론트연결 후 삭제기능 오류 이슈
#### Import 오류 이슈
#### 챗봇 사용시 적절하지 않은 답 이슈
#### 리뷰 작성 및 수정시 500 에러 이슈
#### 데이터베이스 완전 삭제 이슈
#### 회원가입시 500에러 이슈

<br><br>


## 🌐 Architecture

![architecture](https://github.com/user-attachments/assets/377e986d-a234-4b38-a67e-4f974bc9b50d)

<br>

## 📋 ERD Diagram

![ERDiagram](https://github.com/user-attachments/assets/3cb58f82-36d8-4630-a707-483a557ec5a5)

<br>

## 📝 Technologies & Tools (FE) 📝

<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white"/> <img src="https://img.shields.io/badge/CreateReactApp-09D3AC?style=for-the-badge&logo=CreateReactApp&logoColor=white"/> <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=Axios&logoColor=white"/>
<br><img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white"/> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"/> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/>

<br>

## 📝 Technologies & Tools (BE) 📝

<img src="https://img.shields.io/badge/JSONWebToken-000000?style=for-the-badge&logo=JSONWebTokens&logoColor=white"/> <img src="https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=PostgreSQL&logoColor=white"/> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=white"/> <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white"/>

<img src="https://img.shields.io/badge/AmazonEC2-FF9900?style=for-the-badge&logo=AmazonEC2&logoColor=white"/> <img src="https://img.shields.io/badge/AmazonS3-569A31?style=for-the-badge&logo=AmazonS3&logoColor=white"/> <img src="https://img.shields.io/badge/CloudFront-232F3E?style=for-the-badge&logo=Amazon%20AWS&logoColor=white"/> <img src="https://img.shields.io/badge/Route53-FF9900?style=for-the-badge&logo=Amazon%20AWS&logoColor=white"/> 

<img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white"/> <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=nginx&logoColor=white"/> <img src="https://img.shields.io/badge/Daphne-2F855A?style=for-the-badge&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"/>  <img src="https://img.shields.io/badge/GithubActions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>  

<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"/> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white"/>

<br><br><br><br>

<div align=center>

<br>

◻ Copyright ©2024 Team Sparta Final : AI7 team8 all rights reserved.
