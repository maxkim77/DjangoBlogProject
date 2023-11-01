# Django MiniProject1 - Django Technical Blog


![promo](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/142f5a0b-604d-4a36-97d3-44e6f37a7a6a  width="400" height="200")



## 1. 목표와 기능

### 1.1 목표
- Django를 이용한 기술/개발 블로그 개발
- 매일 개발 공부한 지식을 기록하고 유저들에게 전달하기 위한 기술 블로그 개발
- 관리자 외 유저 역시 블로그에 글을 작성 가능하게 끔 개발

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
- 개발환경: Python 3.8, Django 3.2, PostgreSQL
- 배포 URL: http://your-blog.com

## 4. 프로젝트 및 URL 구조와 개발일정

### 4.1 프로젝트 구조
```plaintext
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   ├── base_generic.html
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── form.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
├── static
└── tech_blog
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### 4.2 URL 구조
| App       | URL                | Views Function | HTML File Name | Note           |
|-----------|--------------------|----------------|----------------|----------------|
| accounts  | 'register/'        | register       | register.html  |                 |
| accounts  | 'login/'           | login          | login.html     |                 |
| accounts  | 'loginout/'           | logout          | logout.html     |                 |
| accounts  | 'profile/'           | profile      | profile.html   | 비밀번호변경기능 / 프로필 수정/ 닉네임추가         |
| main      | '/'                | home           | home.html      |                 |
| main      | '/about/'          | about           | about.html   |                 |
| main      | '/generator/'       | generator       | generator.html   |                 |
| blog      | 'blog/'            | blog           | blog.html      |                 |
| blog      | 'blog/<int:pk>/'   | post           | post.html      |                 |
| blog      | 'blog/write/'     | write         | write.html      |  - 카테고리 지정, 사진업로드, 게시글 조회수 반영|
| blog      | 'blog/edit/<int:pk>/' | edit     | edit.html          | - 게시물목록보기 상세보기 반영               |
| blog      | 'blog/delete/<int:pk>/' | delete     | delete.html    | - 삭제후 게시글 목록화면으로 돌아감           |
| blog      | 'blog/search/' | search     | search.html    | - 주제와 카테고리에 따라 검색, 시간순에 따라 정렬|


### 4.3 개발일정
![WBS](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/610b8e27-69ea-43aa-8422-5a9412727493)


- 1주차: 프로젝트 세팅, 모델링, 관리자 페이지 설정
- 2주차: 게시글 CRUD 기능 구현
- 3주차: 로그인/회원가입 기능 구현
- 4주차: 댓글 기능, 이미지 업로드 구현
- 5주차: 추가 기능 구현, 테스팅
- 6주차: 배포 및 최종 테스팅

## 5. UI/BM
- 예시: 메인 페이지, 리스트 페이지, 상세 페이지, 로그인/회원가입 페이지 등

## 6. ERD 모델링
테이블 구조 : 
- users, Post, Comment, Tag, PostLikes, PostTags, UserProfile

  
관계 정의 : 
- Post의 author_id 필드는 users 테이블의 id 필드와 연결,
- PostLikes와 PostTags 테이블은 Post와 User, Post와 Tag 사이의 다대다 관계

![Untitled](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/3e555ca8-9c6c-4f5c-912e-3b8fe7e15aaf)


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
