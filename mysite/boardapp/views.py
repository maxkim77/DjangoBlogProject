from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, BoardComment
from .forms import PostForm, BoardCommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime  

def get_board_post(pk):
    return get_object_or_404(Board, pk=pk) #단축함수 : Board모델에서 기본키가 pk변수값과 일치하는지 조회 주어진 객체가 없는경우 404로 이동 

def increment_view_count(post):
    post.view_count += 1
    post.save()

def handle_like_post(request, post): #좋아요 누르거나 취소
    if request.user in post.board_likes.all():
        post.board_likes.remove(request.user)
    else:
        post.board_likes.add(request.user)

def like_post(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.user in post.board_likes.all():
        post.board_likes.remove(request.user)
    else:
        post.board_likes.add(request.user)
    return redirect('boardapp:post_detail', pk=post.pk)

def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query: #검색어에 따른 필터링
        post_list = Board.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).order_by('-created_at')
    else:
        post_list = Board.objects.all().order_by('-created_at')

    paginator = Paginator(post_list, 5) 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'boardapp/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    post.view_count += 1
    post.save() #save는 메서드
    file_exists = bool(post.file)  # bool은 내장함수 파일의 존재 여부를 확인합니다.
    return render(request, 'boardapp/post_detail.html', {'post': post, 'file_exists': file_exists})

@login_required
def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.created_at = datetime.now()
            post.save()
            return redirect('boardapp:post_detail', pk=post.pk)

    else:  # GET 요청을 처리하는 부분을 추가
        form = PostForm()
    return render(request, 'boardapp/post_write.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Board, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('boardapp:post_detail', pk = post.pk)
    else:
            form = PostForm(instance=post)
    return render(request, 'boardapp/post_edit.html',{'form':form})
    
@login_required
def post_delete(request, pk): #reqeust는 웹요청의 모든데이터, pk 는 주키
    post = get_object_or_404(Board, pk=pk) #만약 해당객체가 없으면 404 없음
    if request.method == "POST": #포스트 방식인지
        post.delete() # 만약 포스트 방식이면 해당 글 삭제
        return redirect('boardapp:post_list') # 게시글 삭제후 사용자를 리다이렉트
    else:
        # GET 요청의 경우 삭제 확인 페이지를 렌더링
        return render(request, 'boardapp/post_delete.html', {'post': post}) # 게시글 삭제확인 페이지 포스트 객체를 컨텍스트에 담아서 템플릿에 전달 이를 통해 포스트 객체 데이터를 사용

@login_required
def comment_create(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardCommentForm(request.POST) #form 은 BoardCommentForm 의 인스턴스 생성
        if form.is_valid(): #폼의 데이터가 유효한지 
            comment = form.save(commit=False) #데이터 베이스에는 아직 저장 x
            comment.author = request.user #댓글 작성자와 해당 댓글이 속할 게시글 을 지정
            comment.post = post  #코멘트 객체에 포스트의 속성을 현재 게시글객체로 설정
            comment.save()
            return redirect('boardapp:post_detail', pk = post.pk) # 댓글 저장후 사용자 해당게시글로 리다이렉션
        else:
            form =BoardCommentForm() #비어있는 새댓글 양식 생성
        return render(request, 'boardapp/comment_form.html',{'form': form}) #댓글양식 컨텍스트로 전달

@login_required
def comment_edit(request, pk, comment_pk): #comment_pk 댓글 인자의
    comment = get_object_or_404(BoardComment, pk=comment_pk)
    if request.method == "POST":
        form = BoardCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('boardapp:post_detail', pk=comment.post.pk)
    else:
        form = BoardCommentForm(instance=comment)
    return render(request, 'boardapp/comment_form.html', {'form': form})
    
@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(BoardComment, pk=comment_pk)
    if request.method == "POST":
        comment.delete()
        return redirect('boardapp:post_detail', pk=comment.post.pk)
    else: 
        return render(request, 'boardapp/comment_confirm_delete.html',{'comment': comment})
    

#직관적이고 명확한 함수뷰, 코드의 중복이 많음