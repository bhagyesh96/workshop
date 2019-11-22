
from django.contrib import admin
from django.urls import path
from django.urls import path, include # new
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')), # new
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
