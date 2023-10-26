from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic.base import RedirectView
import blog.urls
import accounts.urls

urlpatterns = [
    # path('', RedirectView.as_view(pattern_name='blog:blog'), name='root'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls', namespace='blog')),  # blog 앱에 대한 URL 네임스페이스 지정
    path('accounts/', include('accounts.urls', namespace='accounts'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)