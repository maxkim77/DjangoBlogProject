# Django MiniProject1 - Django Technical Blog


![promo](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/142f5a0b-604d-4a36-97d3-44e6f37a7a6a)



## 1. 목표와 기능

### 1.1 목표 및 배경
- 배경: Django를 이용한 AI Image 갤러리형 블로그 개발
- 목표 : 유저들이 Stable Diffusion API를 통해 AI Image 생성후 업로드 및 공유하며 AI Image 정보 공유


### 1.2 기능
- CRUD, 로그인/회원가입, 댓글, 이미지 업로드, 조회수 기능 구현
- 블로그 포스팅: 마크다운 형식으로 글을 작성하고 게시할 수 있습니다.
- 댓글 기능: 각 포스트에 댓글을 작성하고 관리할 수 있습니다.
- 태그 및 카테고리 분류: 포스트를 태그와 카테고리로 분류하여 관리할 수 있습니다.


## 2. 요구사항
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


## 3. 개발환경 및 배포 URL
- 개발환경: HTML, CSS, JS, Bootstrap 5.3, Python 3.8, Django 3.2, PostgreSQL
- 배포 URL: http://your-blog.com

## 4. 프로젝트 및 URL 구조와 개발일정

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
![WBS](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/610b8e27-69ea-43aa-8422-5a9412727493)


| 단계 | 기능 설명 | 상태 |
|------|------------|-------|
| 0단계 | 프로젝트 세팅, 모델링, 관리자 페이지 설정 | ✅ |
| 1단계 | 게시글 CRUD 기능 구현 |  ✅|
| 2단계 | 로그인/회원가입 기능 구현 | ✅ |
| 3단계 | 댓글 기능, 이미지 업로드 구현 | ✅ |
| 4단계 | 추가 기능 구현, 테스팅 | ✅ |
| 5단계 | 배포 및 최종 테스팅 | 🟩 |


## 5. UI 기획


![슬라이드1](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/a738e808-5df8-4ea4-8465-9344b5df46eb)


구성 : 메인 페이지, 설명 페이지, 이미지생성 페이지, 게시판형 블로그 페이지, 갤러리형형 블로그 페이지,로그인/회원가입 페이지 등


## 6. ERD 모델링



![감귤마켓](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/687c5170-1b9a-4f76-bbca-64391dac488d)

테이블 구조 : 
- users, Post, Comment, Tag, PostLikes, PostTags, UserProfile, Board, BoardComment, Boardlikes 

  
관계 정의 : 
- Post와 Board의 author_id 필드는 users 테이블의 id 필드와 연결,
- PostLikes와 PostTags 테이블은 Post와 User, Post와 Tag 사이의 다대다 관계
- BoardComment와 Boardlikes 테이블은 Board, User과 다대일 관계


## 7. 메인기능
- 게시글 작성, 수정, 삭제, 조회
- 로그인/회원가입

## 8. 추가기능
- 댓글 기능
- 이미지 업로드
- 조회수 증가

## 9. 역할 분담 : 김정원(Back-End Developer)

## 10. 느낀점
- Django의 편리함과 Python의 강력함을 느낄 수 있었던 유익한 프로젝트였습니다.

이러한 구조로 프로젝트 문서를 작성하면, 각 섹션별로 더 자세한 내용을 추가하여 프로젝트의 전반적인 계획과 구조를 명확하게 설명할 수 있습니다.
