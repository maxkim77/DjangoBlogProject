from django.urls import path
from .views import HomeView, AboutView, GeneratorView

urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('generator/', GeneratorView.as_view(), name='generator'),
]