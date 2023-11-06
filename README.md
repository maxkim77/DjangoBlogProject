# Django MiniProject1 - Django Technical Blog


![promo](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/142f5a0b-604d-4a36-97d3-44e6f37a7a6a)



## 🎈1. 목표와 기능

### 1.1 목표 및 배경
- 배경:


✔︎ AI Image의 기술의 발달


✔︎ Digital Image 소통의 장 부족에 따른 유저들의 니즈가 있을 것으로 예상되어 블로그 개발


- 목표 :


✔︎ Django를 이용한 AI Image 갤러리형 블로그 개발


✔︎ 유저들이 Stable Diffusion API를 통해 AI Image 생성후 업로드 및 공유하며 AI Image 정보 공유


### 1.2 기능
- CRUD, 로그인/회원가입, 댓글, 이미지 업로드, 조회수 기능 구현
- 블로그 포스팅: 글을 작성하고 게시할 수 있습니다.
- 댓글 기능: 각 포스트에 댓글을 작성하고 관리할 수 있습니다.
- 태그 및 카테고리 분류: 포스트를 태그와 카테고리로 검색 할 수 있습니다.


## 🎉2. 요구사항
### 2.1 기본 요구사항
- UI 스타일링
- 클래스형 뷰 및 함수형 뷰 중 택 개발
- 모놀로식으로 개발
- 데이터 베이스 구조 설계

### 2.2 단계별 요구사항
- 0단계. Django Admin을 이용한 게시글 읽기 및 메인페이지 구현하기
- 1단계: 블로그 CRUD 기능 구현하기
- 2단계: 로그인/회원가입 기능을 이용하여 블로그 구현하기
- 3단계: 블로그 기능 외 추가 기능 작성 및 배포

### 2.3 요구사항 분석 및 아이디어 기획


![캡처](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/a6fd2edb-e205-44f7-9dc5-0424d88a2bb9)


## ✨3. 개발기술 & 환경 및 배포 URL
- 개발 기술 및 환경

[FE]:


![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)


[BE]:


![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23336791.svg?style=for-the-badge&logo=postgresql&logoColor=white)


[API]:


![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-4285F4?style=for-the-badge&logo=stablediffusion&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-008080?style=for-the-badge&logo=openai&logoColor=white)
![tawk.to](https://img.shields.io/badge/tawk.to-1EAE72?style=for-the-badge&logo=tawkto&logoColor=white)


[ENV]:


![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub stars](https://img.shields.io/github/stars/your-username/your-repo?style=social)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?&style=for-the-badge&logo=amazon-aws&logoColor=white)



- 배포 URL: http://your-blog.com

## 🎁4. 프로젝트 및 URL 구조와 개발일정

### 4.1 프로젝트 구조
```plaintext
📦mysite
 ┣ 📂accounts
 ┃ ┣ 📜models.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┣ 📂blog
 ┃ ┣ 📜models.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┣ 📂boardapp
 ┃ ┣ 📜models.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┣ 📂main
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┣ 📂templates
 ┃ ┣ 📂accounts
 ┃ ┣ 📂blog
 ┃ ┣ 📂boardapp
 ┃ ┣ 📂main
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┣ 📂media
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📂images
 ┣ 📂tutorialdjango
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┗ 📜manage.py

```

### 4.2 URL 구조
- main

  
| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| main      | '/'                                        | home              | main/home.html                        |                |
| main      | '/about/'                                  | about             | main/about.html                       |                |
| main      | '/generator/'                               | generator         | main/generator.html                   |                |


- accounts

  
| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| accounts  | 'register/'                                | register          | accounts/register.html                |                |
| accounts  | 'login/'                                   | login             | accounts/login.html                   |                |
| accounts  | 'logout/'                                  | logout            | accounts/logout.html                  |                |
| accounts  | 'profile/'                                 | profile           | accounts/profile.html                 | 비밀번호변경기능 / <br>프로필 수정/ 닉네임추가 |


- boardapp


| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| boardapp  | 'board/'                                   | board             | boardapp/post_list.html               | 게시판 목록 |
| boardapp  | 'board/<int:pk>/'                          | post_detail       | boardapp/post_detail.html            | 게시글 상세보기 |
| boardapp  | 'board/write/'                             | post_write        | boardapp/post_write.html             | 게시글 작성 |
| boardapp  | 'board/edit/<int:pk>/'                     | post_edit         | boardapp/post_edit.html              | 게시글 수정 |
| boardapp  | 'board/delete/<int:pk>/'                   | post_delete       | boardapp/post_delete.html            | 게시글 삭제 |
| boardapp  | 'board/<int:pk>/comment/'                  | comment_create    | boardapp/comment_form.html           | 댓글 작성 |
| boardapp  | 'board/<int:pk>/comment/<br><int:comment_pk>/edit/' | comment_edit | boardapp/comment_form.html           | 댓글 수정 |
| boardapp  | 'board/<int:pk>/comment/<br><int:comment_pk>/delete/' | comment_delete | boardapp/comment_<br>confirm_delete.html| 댓글 삭제 |


- blog


| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| blog      | 'blog/'                                    | blog              | blog/blog.html                        |                |
| blog      | 'blog/<int:pk>/'                           | post              | blog/post.html                        |                |
| blog      | 'blog/write/'                              | write             | blog/write.html                       | 카테고리 지정, 사진업로드,<br> 게시글 조회수 반영|
| blog      | 'blog/edit/<int:pk>/'                      | edit              | blog/edit.html                        | 게시물목록보기 |
| blog      | 'blog/delete/<int:pk>/'                    | delete            | blog/delete.html                      |                 |
| blog      | 'blog/search/'                             | search            | blog/search.html                      | 주제와 카테고리에 따라 검색,<br> 시간순에 따라 정렬|
| blog      | 'post/<int:post_pk>/comment/'              | comment_new       | blog/comment_form.html                |                |
| blog      | 'post/<int:post_pk>/comment/<br><int:parent_pk>/' | reply_new    | blog/comment_form.html                |                |
| blog      | 'post/<int:pk>/like/'                      | like_post         | blog/post.html                        |                |
| blog      | 'comment/<int:pk>/update/'                 | comment_update    | blog/comment_form.html                |                |
| blog      | 'comment/<int:pk>/delete/'                 | comment_delete    | blog/comment_<br>confirm_delete.html      |                |





### 4.3 개발일정


![슬라이드2](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/4da10f41-94e7-47df-ab20-de7bf4dccc53)


## 🎉5. UI 기획


![슬라이드1](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/a738e808-5df8-4ea4-8465-9344b5df46eb)


구성 : 메인 페이지, 설명 페이지, 이미지생성 페이지, 게시판형 블로그 페이지, 갤러리형형 블로그 페이지,로그인/회원가입 페이지 등


## 🎨6. ERD 모델링



![감귤마켓](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/687c5170-1b9a-4f76-bbca-64391dac488d)

테이블 구조 : 
- users, Post, Comment, Tag, PostLikes, PostTags, UserProfile, Board, BoardComment, Boardlikes 

  
관계 정의 : 
- Post와 Board의 author_id 필드는 users 테이블의 id 필드와 연결,
- PostLikes와 PostTags 테이블은 Post와 User, Post와 Tag 사이의 다대다 관계
- BoardComment와 Boardlikes 테이블은 Board, User과 다대일 관계


## 🎲7. 메인기능
📌 메인페이지 구현

  ![1](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/c7cfc8a1-a39e-404e-9647-aac57c06d8d4)

- 페이지 제목과 블로그 입장하기 버튼이 있습니다.
- 회원가입/로그인 버튼이 있습니다.
- 회원가입 버튼을 클릭하면 회원가입 페이지로 이동합니다.
- 로그인 버튼을 클릭하면 로그인 페이지로 이동합니다.


## 🔔8. 추가기능
- 댓글 기능
- 이미지 업로드
- 조회수 증가

## 🧑9. 역할 분담 : 김정원(Back-End Developer)

## 📖10. 느낀점
- Django의 편리함과 Python의 강력함을 느낄 수 있었던 유익한 프로젝트였습니다.

이러한 구조로 프로젝트 문서를 작성하면, 각 섹션별로 더 자세한 내용을 추가하여 프로젝트의 전반적인 계획과 구조를 명확하게 설명할 수 있습니다.
