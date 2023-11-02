from typing import Any
from urllib import request
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
# import os
from django.views import View
from .models import Post
from django.urls import reverse_lazy

class PostDetailView(DetailView):
    template_name = 'blog/post.html'
    model = Post
    
    # def get(self, request, *args, **kwargs):
    #     post = Post.objects.get(pk=kwargs['pk'])
    #     file_extension = os.path.splitext(post.file_upload.url)[1] if post.file_upload else None
    #     return render(request, 'blog/post.html', {'post':post, 'file_extension': file_extension})
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1 #조회수 증가
        obj.save(update_fields=['view_count'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['main_comments'] = post.comments.filter(parent__isnull=True)
        context['comment_form'] = CommentForm()
        context['tags'] = post.tags.all() 
        return context
    
post = PostDetailView.as_view()

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/write.html'
    model = Post
    fields = ['category','title', 'content', 'thumb_image', 'image','file_upload','tags']
    success_url = reverse_lazy('blog:blog')

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/edit.html'
    model = Post
    context_object_name = 'post'
    fields = ['category','title', 'content', 'thumb_image', 'image','file_upload','tags']
    success_url = reverse_lazy('blog:blog')

    def test_func(self):
        post = self.get_object()
        return self.new_method(post)

    def new_method(self, post):
        return post.author == self.request.user

edit = UpdatePostView.as_view()

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:blog')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class SearchView(ListView):
    template_name = 'blog/search.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query).order_by('-created_at')
        return Post.objects.all().order_by('-created_at')  # 검색어가 없으면 전체 게시글 반환

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        result = self.get_queryset()

        # Paginator 설정
        paginator = Paginator(result, 10)  # 페이지당 10개의 결과
        page_number = self.request.GET.get('page') or 1
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['query'] = query  # 검색어 추가
        return context

# views.py
from django.urls import reverse

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
        parent_pk = self.kwargs.get('parent_pk')
        if parent_pk:
            form.instance.parent = Comment.objects.get(pk=parent_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', kwargs={'pk': self.object.post.pk})

class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['message']
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('blog:blog')

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('blog:post_detail', kwargs={'pk': comment.post.pk})
    

class BlogListView(ListView):
    template_name = 'blog/blog.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4  # 일반 게시글 페이지네이션 설정
    ordering = ['-created_at']  # 역순 정렬 설정

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 공지사항과 일반 게시글을 역순으로 정렬
        notice_list = Post.objects.filter(is_notice=True).order_by('-created_at')
        regular_post_list = Post.objects.filter(is_notice=False).order_by('-created_at')

        # Paginator 설정
        notice_paginator = Paginator(notice_list, 2)  # 페이지당 2개의 공지사항
        regular_post_paginator = Paginator(regular_post_list, 4)  # 페이지당 4개의 일반 게시글

        notice_page_number = self.request.GET.get('notice_page') or 1
        regular_post_page_number = self.request.GET.get('regular_page') or 1

        context['notices'] = notice_paginator.get_page(notice_page_number)
        context['regular_posts'] = regular_post_paginator.get_page(regular_post_page_number)

        return context

    def get_queryset(self):
        # 기본 쿼리셋은 'created_at'을 기준으로 역순 정렬
        return Post.objects.all().order_by('-created_at')

from django.shortcuts import get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('blog:post', pk=post.pk)
