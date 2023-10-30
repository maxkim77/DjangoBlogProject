from django.urls import reverse
from django.db import models
from django.conf import settings
import django.utils.timezone
from django.contrib import admin

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    thumb_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank=True, null=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank = True)
    is_notice = models.BooleanField(default=False, verbose_name="공지사항 여부") #추가

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return self.message
    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def is_reply(self):
        return self.parent is not None
    
    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.post.pk})
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_notice']
    # 기타 설정들...