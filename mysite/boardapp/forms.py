from django import forms
from .models import Board, BoardComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['category', 'title', 'content', 'file']

    category = forms.ChoiceField(choices=[('Knowledge', 'Knowledge'), ('SmallTalk', 'SmallTalk')], widget=forms.Select(attrs={'class': 'form-select'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

class BoardCommentForm(forms.ModelForm):
    class Meta:
        model = BoardComment
        fields =['content']


#widget=forms.Select(attrs={'class':'form-select'})
#이필드는 드롭다운 선택메뉴
#BoardComment 모델의 content 필드만 폼에서 사용됨을 지정