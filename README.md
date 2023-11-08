# Django MiniProject1 - Django Technical Blog


![promo](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/142f5a0b-604d-4a36-97d3-44e6f37a7a6a)



## 🎈1. 목표와 기능

### 1.1 목표 및 배경
- 목표 :


✔︎ Django를 이용한 AI Image 갤러리형 블로그 개발


✔︎ 유저들이 Stable Diffusion API를 통해 AI Image 생성후 업로드 및 공유하며 AI Image와 관련 정보 공유


- 배경:


✔︎ Stable Diffusion, Dalle 등 AI Image의 기술의 발달


✔︎ AI 이미지에 대한 관심과 AI이미지용 블로그 주제가 많이 없다고 생각되어 해당 주제로 블로그 개발


### 1.2 기능
- CRUD, 로그인/회원가입, 댓글, 이미지 업로드, 조회수 기능 구현
- 블로그 포스팅
- 댓글 기능
- 태그 및 카테고리 분류
  

## 🎉2. 요구사항
### 2.1 기본 요구사항
- UI 스타일링
- 클래스형 뷰 및 함수형 뷰 중 택 개발
- 데이터 베이스 구조 설계
- 모놀로그식 장고


### 2.2 단계별 요구사항
- 0단계: Django Admin을 이용한 게시글 읽기 및 메인페이지 구현하기
- 1단계: 블로그 CRUD 기능 구현하기
- 2단계: 로그인/회원가입 기능을 이용하여 블로그 구현하기
- 3단계: 블로그 기능 외 추가 기능 작성 및 배포

### 2.3 요구사항 분석 및 아이디어 기획


![캡처](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/a6fd2edb-e205-44f7-9dc5-0424d88a2bb9)


- 4개의 앱(main, accounts, blog(메인 갤러리형 게시판), boardapp(보조형 자유게시판))으로 구성

- 클래스뷰 및 함수형뷰
    - 클래스 뷰는 제너릭뷰, 믹스인뷰을 사용할 수 있는 '확장성'과 '재사용성'이라는 장점으로 주요 앱(main, accounts,blog) 는 클래스형으로 작성
    - 함수형 뷰는 '간결'하고 '직관'적인 특징으로 간편하게 쓰일 수있는 보조형 자유게시판에서 작성
      
- 포스트 기능으로 좋아요, 태그, 대댓글, 카테고리 등을 사용 함
    - 댓글은 메인 갤러리형 블로그는 대댓글형
    - 보조 자유 게시판은 일반 댓글형 구현


## ✨3. 개발기술 & 환경 및 배포 URL
### 3.1 개발 기술 및 환경

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
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?&style=for-the-badge&logo=amazon-aws&logoColor=white)
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>

- 부트스트랩은 Startbootstrap에서 테마를 따옴
- 특이사항으로는 tawk.to라는 실시간 채팅솔루션과 StableDiffusion API로 이미지 생성 가능하게 함(배포 버젼에서는 현재는 토큰수 소진으로 생성이 안되는 상황)
- Github에 업로드한 레파지토리를 AWS lightsail에 clone 하여 배포
  
### 3.2 배포 URL: http://54.180.146.126:8000/


## 🎁4. 프로젝트 및 URL 구조와 개발일정

### 4.1 프로젝트 구조


- 프로젝트 구조는 아래와 같이 accounts, blog, boardapp, main 4개로 구성됨

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
| main      | '/'                                        | home              | main/home.html                        | 홈화면          |
| main      | '/about/'                                  | about             | main/about.html                       | 소개화면               |
| main      | '/generator/'                               | generator         | main/generator.html                   | AI이미지 생성게시판      |


- accounts

  
| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| accounts  | 'register/'                                | register          | accounts/register.html                |회원가입         |
| accounts  | 'login/'                                   | login             | accounts/login.html                   |로그인           |
| accounts  | 'logout/'                                  | logout            | accounts/logout.html                  |로그아웃         |
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
| blog      | 'blog/'                                    | blog              | blog/blog.html                        |갤러리형 게시판 메인 화면  |
| blog      | 'blog/<int:pk>/'                           | post              | blog/post.html                        |상세 포스트 화면    |
| blog      | 'blog/write/'                              | write             | blog/write.html                       | 카테고리 지정, 사진업로드,<br> 게시글 조회수 반영|
| blog      | 'blog/edit/<int:pk>/'                      | edit              | blog/edit.html                        | 게시물목록보기 |
| blog      | 'blog/delete/<int:pk>/'                    | delete            | blog/delete.html                      | 삭제 화면      |
| blog      | 'blog/search/'                             | search            | blog/search.html                      | 주제와 카테고리에 따라 검색,<br> 시간순에 따라 정렬|
| blog      | 'post/<int:post_pk>/comment/'              | comment_new       | blog/comment_form.html                | 댓글 입력 폼     |
| blog      | 'post/<int:post_pk>/comment/<br><int:parent_pk>/' | reply_new    | blog/comment_form.html                | 대댓글 폼      |
| blog      | 'post/<int:pk>/like/'                      | like_post         | blog/post.html                        |좋아요를 누르면 blog/post로 Redirect됨|
| blog      | 'comment/<int:pk>/update/'                 | comment_update    | blog/comment_form.html                |댓글 업데이터 경로   |
| blog      | 'comment/<int:pk>/delete/'                 | comment_delete    | blog/comment_<br>confirm_delete.html      |댓글 삭제 폼    |





### 4.3 개발일정


![슬라이드2](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/4da10f41-94e7-47df-ab20-de7bf4dccc53)


## 🎉5. UI 기획 및 구성


![슬라이드1](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/a738e808-5df8-4ea4-8465-9344b5df46eb)


### 5.1 main 구성 : 
- 메인 페이지
- 설명 페이지
- 이미지생성 페이지


### 5.2 boardapp 구성:
- 게시판형 블로그 페이지


### 5.3 blog 구성:
- 갤러리형 블로그 페이지


### 5.4 accounts 구성:
- 로그인/회원가입 페이지 등


## 🎨6. ERD 모델링


![감귤마켓](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/687c5170-1b9a-4f76-bbca-64391dac488d)


### 6.1 테이블 구조 : 
- users, Post, Comment, Tag, PostLikes, PostTags, UserProfile, Board, BoardComment, Boardlikes(총 10개의 테이블)

  
### 6.2 관계 정의 : 
- Post와 Board의 id 필드는 users 테이블의 id 필드와 연결
- 다대다 관계 : PostLikes ↔ (Post 와 User) / PostTags ↔ (Post 와 Tag)
- 다대일 관계 : BoardComment - Board / Boardlikes - User


## 🎲7. 메인기능
📌 메인페이지 구현


![1 (2)](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/4c3592bc-0bb1-45c7-bca8-6d8ee0a11e08)

- 페이지 제목과 블로그 입장하기 버튼
- 회원가입/로그인 버튼
- 회원가입 버튼을 클릭하면 회원가입 페이지로 이동
- 로그인 버튼을 클릭하면 로그인 페이지로 이동


📌 회원가입 / 로그인 기능 구현


![3 (1)](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/11c97b55-d0c3-4afe-b023-e19dffa74dbd)


- 회원가입을 할 수 있는 페이지
- 입력받는 값은 id, password
- 로그인을 할 수 있는 페이지
- 입력받는 값은 id, password


📌 게시글 작성 기능 구현


![4 (2)](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/73c51c68-5d77-4599-b79a-250e8c19e467)


- 로그인을 한 유저만 해당 기능을 사용 할 수 있음
- 게시글 제목과 내용을 작성 할 수 있는 페이지가 있음
- 작성한 게시글이 저장되어 게시글 목록에 보여야 함
- **사진 업로드가 가능하도록 함**
- **게시글 조회수가 올라갈 수 있도록 함**


📌 게시글 목록 기능 구현


![2](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/946643a3-1f37-40ac-adf4-45845beeb335)
![1](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/5576424f-d1dd-4e28-bebb-4f220897442a)


- 모든 사용자들이 게시한 블로그 게시글들의 제목을 확인 함


📌 게시글 상세보기 기능 구현
![5](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/8cb98248-277c-46f0-95f9-bdc5e9a8a1a0)
![3](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/9bb70576-3b8c-43ac-b607-99fd53fdd173)

 
- 게시글의 제목/내용을 보는 기능


📌 게시글 검색 기능 구현
![6](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/5c0ef061-1ac8-4af8-a7ad-24eb43af182f)


- 주제와 태그에 따라 검색이 가능
- 검색한 게시물은 최신순에 따라 정렬


📌 게시글 수정 기능 구현


![8](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/1f19428d-ef40-464e-99e5-b1dc305f64e7)


- 로그인을 한 유저만 해당 기능 사용 가능
- 본인의 게시글이 아니라면 수정이 불가능
- 게시글의 제목 또는 내용을 수정 하는 기능
- 수정된 내용은 게시글 목록보기/상세보기에 반영


📌  게시글 삭제 기능 구현


![9](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/98a283e3-4f60-45c3-8559-2a062e994e4c)


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


![11 (3)](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/1ffadcda-8ff4-4981-9eb7-821305df5482)

 
 - 댓글 추가
 - 댓글 편집/삭제
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


- 공지사항 기능
    - 관리자만 관리자페이지에서 설정 가능
    - 모델에서 is_notice 설정
    - views.py에서 get_context_data 메서드를 사용하여 공지사항과 일반 게시글을 분리
  

![13](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/e0fe3bb4-8b8f-44fe-bac3-abdbfefd59eb)


![image](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/b450ec07-3a84-45ff-8d2a-ec771b283355)


```   
# models.py
class Post(models.Model):
# <생략>
    is_notice = models.BooleanField(default=False, verbose_name="공지사항 여부")
# views.py
class BlogListView(ListView):
# <생략>
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notice_list = Post.objects.filter(is_notice=True).order_by('-created_at')
        regular_post_list = Post.objects.filter(is_notice=False).order_by('-created_at')
# <생략> 
```      


- Tawk API를 활용한 실시간 채팅기능(About 페이지)


![2 (2)](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/5f3269e1-da7e-4efc-984e-2107e757cf50)


🎈 Link : https://www.tawk.to/

- Stable Diffusion을 활용한 AI 이미지 생성 화면(Generator 페이지)


![12 (3)](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/9ef7652c-fc2c-4faf-adbc-80007c424287)


🎈 Link : https://stablediffusionapi.com/docs/stable-diffusion-api/text2img

📍 **(선택) AWS Lightsail로 배포**


![image](https://github.com/maxkim77/DjangoBlogProject/assets/141907655/eae3e876-d441-43e5-a860-3c83097ab09c)

🎈 Link : https://aws.amazon.com/ko/lightsail/


https://github.com/maxkim77/DjangoBlogProject/assets/141907655/7ffb27ae-7f88-4695-97ef-19f180e84ca2


## 🧑9. 개발자 : 김정원(Back-End Developer)



## 📖 10. 총 정리


### 10.1 오류정리

**🛠IntegrityError**
- 에러명: 'IntegrityError'
- 문제상황: 모델 필드가 null 값을 허용 안함
- 해결방안: 해당 필드에 'null=True' 옵션 추가

```python
# models.py
summary = models.TextField(null=True)
```


### 10.2 알게된 점

💡 **클래스형 뷰 목록**

- 제너릭뷰
  - ListView: 게시목록을 보여 줌
  - DetailView: 게시물 상세 정보 보여 줌
  - CreateView: 새로운 객체를 생성
  - UpdateView: 기존 객체를 수정
  - DeleteView: 객체를 삭제할 때 사용
  - TemplateView: 정적 페이지를 렌더링

- 믹스인(Mixins)
  - LoginRequiredMixin: 사용자가 로그인 해야만 접근 할 수 있는 뷰
  - UserPssesTextMixin: 사용자가 특정 텍스트를 통과해야만 뷰에 접근

💡 **django-widget-tweaks**
- Django의 폼 필드의 HTML을 보다 쉽게 제어할 수 있게 해주는 라이브러리 CSS 클래스 추가, 속성 변경 가능

```html
{% load widget_tweaks %}
<form method="post">
    {% csrf_token %}
</form>
```

```html
{% render_field form.field_name class="form-control" %} # 필드 특정 조건에 따라 렌더링하고 싶을 때 사용
{{ field|add_class:"form-control" }} # | 기호는 필터를 의미 이 필터는 지정된 필드에 클래스를 추가
```

본 프로젝트에서는 두 번째 방식으로 클래스에 부트스트랩 클래스를 추가하여 디자인 하였음

💡 **대댓글 구현 방식**
- Comment 모델의 parent 필드를 통해 구현
- 사용자가 B라는 댓글을 달 때 A의 대댓글로 지정하려는 경우, A라는 대댓글 ID는 parent_pk 파라미터로 전달
- CommentCreateView 에서 이를 확인하여 B 댓글의 부모댓글 'parent' 댓글로 A를 설정
- 이렇듯 parent 필드를 통해 부모-자식간의 관계가 형성됨
- 템플릿에서는 주댓글에 대한 루프를 돌면서 replies 관계 형성

```html
{% for reply in comment.replies.all %}
{% endfor %}
```

### 10.3 느낀점

- Django의 편리함과 Python의 강력함을 느낄 수 있었던 유익한 프로젝트였음
- 스프링부트 자바 강의를 조금씩 듣고 있는데 많은 경험이 있는건 아니지만 따른 프레임 워크에 비해 효율적이고 빠르게 게시판을 만들 수 있음을 느낌
- 함수형과 클래스형 뷰 코드를 모두 사용해보기 위해 앱 개수가 늘어나다 보니 URL이 복잡해졌지만, 둘의 차이점에 대해 알 수 있었음
- 장고의 다양한 기능과 코드 방식에 대해 깊이 연구 할 수 있는 기회가 됨
- AWS 배포를 통해 아마존 웹 서비스를 처음 활용 해볼 수 있는 좋은 기회가 됨
