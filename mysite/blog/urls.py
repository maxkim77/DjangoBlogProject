from . import views 
from django.urls import path
from .views import BlogListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, SearchView, CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<int:pk>/', PostDetailView.as_view(), name='post'),
    path('write/', CreatePostView.as_view(), name ='write'),
    path('edit/<int:pk>/', UpdatePostView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('post/<int:post_pk>/comment/', CommentCreateView.as_view(), name='comment_new'),
    path('post/<int:post_pk>/comment/<int:parent_pk>/', CommentCreateView.as_view(), name='reply_new'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

# urls.py
from django.conf.urls import handler404
handler404 = 'blog.views.handler404'
