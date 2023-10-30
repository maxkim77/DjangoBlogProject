from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'thumb_image', 'image','file_upload','tags']
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # commit이 False인 경우, ManyToMany 필드는 저장되지 않습니다.
        # 따라서, save_m2m() 메소드를 호출해야 합니다.
        if commit:
            instance.save()
            self.save_m2m()  # 태그 필드 저장

        return instance    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
