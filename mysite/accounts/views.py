from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .forms import UserAndProfileForm
from .models import UserProfile

#계정 생성 -> 로그인 -> 로그아웃 -> 프로필 보기/수정 -> 비밀번호 변경 순
class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'

class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('accounts:login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserAndProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')

# reverse_lazy 리다이렉션 함수