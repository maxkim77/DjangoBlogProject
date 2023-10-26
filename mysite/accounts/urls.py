from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, ChangePasswordView, ProfileEditView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
     # 프로필 수정 URL
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),

    # 비밀번호 변경 URL
    path('profile/change-password/', ChangePasswordView.as_view(), name='change_password'),
]