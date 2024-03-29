from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/conf/', include('rest_framework.urls')),
    path('api/geral/', include('common.urls')),
    path('api/medicina/', include('medicina.urls'))
]
