from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, ChangePasswordView, ProfileEditView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change_password'),
]