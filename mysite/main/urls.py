from django.urls import path
from .views import HomeView, AboutView, GeneratorView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('generator/', GeneratorView.as_view(), name='generator'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
