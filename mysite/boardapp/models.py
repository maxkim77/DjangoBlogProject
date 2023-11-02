from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    category = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True, null=True)    
    view_count = models.PositiveIntegerField(default=0)
    # tags = models.ManyToManyField('Tag', blank = True)
    board_likes = models.ManyToManyField(User, related_name='board_likes', blank = True)

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.board_likes.count()
    
class BoardComment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="board_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

