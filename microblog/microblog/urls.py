"""
URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog.views import CreateUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include([
        path('register/', CreateUserView.as_view(), name='create-user'),
        path('', include('django.contrib.auth.urls')),
    ])),
    path('blog/', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
