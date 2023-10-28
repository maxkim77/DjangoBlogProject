from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm


from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    template_name = 'blog/blog.html'
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'blog/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['main_comments'] = post.comments.filter(parent__isnull=True)
        context['comment_form'] = CommentForm()
        return context
    
post = PostDetailView.as_view()

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/write.html'
    model = Post
    fields = ['category', 'title', 'content', 'tags', 'image']
    success_url = reverse_lazy('blog:blog')

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/edit.html'
    model = Post
    context_object_name = 'post'
    fields = ['category', 'title', 'content', 'tags', 'image']
    success_url = reverse_lazy('blog:blog')

    def test_func(self):
        post = self.get_object()
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
            return Post.objects.filter(title__icontains=query)
        return super().get_queryset()

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