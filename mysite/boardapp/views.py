import logging
from django.shortcuts import redirect, render, get_object_or_404
from .models import Board, BoardComment
from .forms import PostForm, BoardCommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
# import logging

def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
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
    post.save()
    file_exists = bool(post.file)  # 파일의 존재 여부를 확인합니다.
    return render(request, 'boardapp/post_detail.html', {'post': post, 'file_exists': file_exists})


def like_post(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.user in post.board_likes.all():
        post.board_likes.remove(request.user)
    else:
        post.board_likes.add(request.user)
    return redirect('boardapp:post_detail', pk=post.pk)

@login_required
def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
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
def post_delete(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('boardapp:post_list')
    else:
        # GET 요청의 경우 삭제 확인 페이지를 렌더링
        return render(request, 'boardapp/post_delete.html', {'post': post})
    
@login_required
def comment_edit(request, pk, comment_pk):
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
def comment_create(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('boardapp:post_detail', pk = post.pk)
        else:
            form =BoardCommentForm()
        return render(request, 'boardapp/comment_form.html',{'form': form})
    
@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(BoardComment, pk=comment_pk)
    if request.method == "POST":
        comment.delete()
        return redirect('boardapp:post_detail', pk=comment.post.pk)
    else: 
        return render(request, 'boardapp/comment_confirm_delete.html',{'comment': comment})