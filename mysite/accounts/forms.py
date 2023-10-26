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
