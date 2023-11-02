from django.urls import path
from . import views

app_name = 'boardapp'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/write/', views.post_write, name='post_write'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('post/<int:pk>/comment/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('post/<int:pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]

