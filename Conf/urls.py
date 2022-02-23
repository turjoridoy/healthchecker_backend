from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v0/', include('apps.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "Health Checker"
admin.site.site_title = "Health Checker Admin Portal"
admin.site.index_title = "Welcome to Health Checker Admin Portal"
