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

- 페이지 제목과 블로그 입장하기 버튼
- 회원가입/로그인 버튼
- 회원가입 버튼을 클릭하면 회원가입 페이지로 이동
- 로그인 버튼을 클릭하면 로그인 페이지로 이동


📌 회원가입 기능 구현

![3](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/f2b9dd7b-ea74-4858-b853-f6a828d2b78a)


- 회원가입을 할 수 있는 페이지
- 입력받는 값은 id, password


📌 로그인 기능 구현


![2](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/f95a4d9a-34d3-4b71-97aa-c6758c383e8f)


- 로그인을 할 수 있는 페이지
- 입력받는 값은 id, password


📌 게시글 작성 기능 구현


![4](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/eaf77c4d-31f8-4b1c-8bd5-afa998e44ae6)


- 로그인을 한 유저만 해당 기능을 사용 할 수 있음
- 게시글 제목과 내용을 작성 할 수 있는 페이지가 있음
- 작성한 게시글이 저장되어 게시글 목록에 보여야 함
- **사진 업로드가 가능하도록 함**
- **게시글 조회수가 올라갈 수 있도록 함**


📌 게시글 목록 기능 구현
![7](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/db0c977f-9ce4-4a99-b5a9-214177a44023)
![6](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/e6c9c133-ad28-440c-9050-e574235c99fe)


- 모든 사용자들이 게시한 블로그 게시글들의 제목을 확인 함


📌 게시글 상세보기 기능 구현
![8](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/c9b7acf5-70b4-4d8e-8a26-8eb4a7d4828a)
![9](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/f44f1467-5398-44ea-86d8-9cbd3be19443)

 
- 게시글의 제목/내용을 보는 기능


📌 게시글 검색 기능 구현
![10](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/4f2e87ea-421e-4091-8da9-95427cbda230)


- 주제와 태그에 따라 검색이 가능
- 검색한 게시물은 최신순에 따라 정렬


📌 게시글 수정 기능 구현

![11](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/19c1945a-ceb8-46bd-b28c-6674f575b4ef)


- 로그인을 한 유저만 해당 기능 사용 가능
- 본인의 게시글이 아니라면 수정이 불가능
- 게시글의 제목 또는 내용을 수정 하는 기능
- 게시글 제목과 내용을 수정 할 수 있는 페이지 유
- 수정된 내용은 게시글 목록보기/상세보기에 반영


📌  게시글 삭제 기능 구현


![12-1](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/cd0b949d-f0da-4b4a-bfc6-45574471970f)


- 로그인을 한 유저만 해당 기능을 사용 할 수 있음
- 본인의 게시글이 아니라면 수정이 불가
- 게시글을 삭제하는 기능
- 삭제를 완료한 이후에 게시글 목록 화면으로 돌아감
- 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가


## 🔔8. 추가기능
📍 **회원 관련 추가 기능(UI 직접 구현 필요)**


![13](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/8c74da30-4129-4b53-bdda-ffa2e71edc51)


- 비밀번호 변경기능
- 프로필 수정
- 닉네임(Username) 추가


📍 **댓글 기능(UI 직접 구현 필요)**

 ![14-min](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/11e4da59-1513-445a-8862-36ac54aaa97c)

 
 - 댓글 추가
 - 댓글 삭제
 - 대댓글


📍 부가 기능
- 정적 파일 모으기 (collectstatic)

```
# settings.py

# 정적 파일 기본 URL
STATIC_URL = '/static/'

# 추가적인 정적 파일 디렉토리 (개발 환경에서 사용)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
#(운영환경에서 사용)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
서버에서 python manage.py collectstatic 명령 입력

- Tawk API를 활용한 실시간 채팅기능(About 페이지)


![16](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/b1baeb2b-98da-47a9-8eca-fa1c35e8d57a)



- Stable Diffusion을 활용한 AI 이미지 생성 화면(Generator 페이지)


![15](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/08b63f0c-87ac-4661-bfe2-d9e7ce615180)


📍 **(선택) AWS Lightsail로 배포**


![image](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/eae3e876-d441-43e5-a860-3c83097ab09c)



https://github.com/maxkim77/DjangoBlogProject/assets/141907655/01223160-76a2-4f36-b6d9-1ae525a23099


## 🧑9. 개발자 : 김정원(Back-End Developer)



## 📖10. 총 정리
- 오류정리

  
    - **SyntaxError in Views.py**
    - 에러명: 'SyntaxError'
    - 문제코드: 'if request.method = "POST":
    - 해결방안: 파이썬 조건문에서는 동등비교를 위해 '=='을 사용해야 함
    ```
    if request.method == "POST":
    ```


    - **IntegerityError**
    - 에러명 : 'IntegrityError'
    - 문제상황 : 모델필드가 null 값을 허용 안함
    - 해결방안 : 해당 필드에 'null=True' 옵션추가
    ```
    #models.py
    summary = models.TextFeild(null=True)
    ```


    - **파일 업로드 후 표시문제**
    - 에러명: ValueError
    - 문제상황 : 템플릿에서 파일 확장자와 맞지 않는 파일을 올릴때는 표시가 안 되었음
    - 해결방안: post_detail 뷰에서 파일 존재여부 확인후 이를 템플릿에 전달, 템플릿에서는 file_exists 변수를 사용하여 조건부 렌더링 수행, 다음과 같이 뷰 및 템플릿 수정
    ```
    def post_detail(request, pk):
        post = get_object_or_404(Board, pk=pk)
        post.view_count += 1
        file_exists = bool(post.file)
        return render(request, 'boardapp/post_detail.html', {'post': post, 'file_exists': file_exists})
    ```
    ```
    {% if file_exists %}
        {% with file_extension = post.file.url|slice:"-5:" %}
        <!-- --!>
        {% endwith %}
    {% endif %}       
    ```

       
- 느낀점
    - Django의 편리함과 Python의 강력함을 느낄 수 있었던 유익한 프로젝트였음
    - 스프링부트 자바 강의를 조금씩 듣고 있는데 많은 경험이 있는건 아니지만 따른 프레임 워크에 비해 효율적이고 빠르게 게시판을 만들 수 있음을 느낌
    - 함수형과 클래스형 뷰 코드를 모두 사용해보기 위해 앱 개수가 늘어나다 보니 URL이 복잡해졌지만, 둘의 차이점에 대해 알 수 있었음 
