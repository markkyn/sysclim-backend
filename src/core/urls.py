from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.controllers import index

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name="index"),

    path('api/geral/', include('common.urls')),
    path('api/medicina/', include('medicina.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
