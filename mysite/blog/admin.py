from django.contrib import admin
from .models import Post, Comment, Tag, PostAdmin

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)