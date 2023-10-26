from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import UserAndProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
# 필요한 추가 임포트...

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

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')

# 프로필 수정 뷰
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserAndProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user
