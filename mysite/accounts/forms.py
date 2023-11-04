from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserAndProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserAndProfileForm, self).__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'userprofile'):
            self.fields['address'].initial = self.instance.userprofile.address
            self.fields['phone'].initial = self.instance.userprofile.phone

    def save(self, commit=True):
        user = super(UserAndProfileForm, self).save(commit=commit)
        profile, created = UserProfile.objects.get_or_create(user=user)

        profile.address = self.cleaned_data['address']
        profile.phone = self.cleaned_data['phone']
        if commit:
            profile.save()
        return user

#ModelForm: 모델의 데이터를 폼에 쉽게 바인딩할수 있도록 Model Form 클래스제공
#이를 사용하면 모델인스턴스 기반으로 폼을 생성하고 폼의 데이터를 모델인스턴스에 저장하는 과정 간소화 가능
#폼필드확장: User 모델 과 연관된 UserProfile 모델 필드(address, phone)를 폼에 추가
#User 모델 필드(username,email,first_name,lastname)뿐만아니라 UserProfile의 address와 phone 필드도 함께 제출
#코드 분석
# class Meta:
# model = User 폼이 모델과 연결
#fields = ['username', 'email', 'first_name', 'last_name'] 폼에 포함될 User모델의 필드를 지정
#__init__ 메소드
#폼인스턴스가 생성될때 address와 phone 정보를 같이 불러오기 위함
#if self.instance and hasattr(self.instance, 'userprofile')
#user = super(UserAndProfileForm, self).save(commit=commit);
#이 줄은 먼저 UserAndProfileForm의 부모 클래스의 save메서드를 호출 이는 모델데이터 저장
# commit 인자가 True이면 폼데이터는 모델의 데이터를 저장
#commit 인자가 True 이면 폼데이터는 데이터베이스에 즉시저장 Fale라면 데이터는 저장 x User 모델인스턴스만 반환
#profile, created= User.Profile 인스턴스르 찾거나 새로생성 getor created는 객체가 이미존재하면 새객체 반환
# return user: 마지막으로 suer 모델 인스턴스 반환