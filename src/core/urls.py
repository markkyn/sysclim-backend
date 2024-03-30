from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,)

from common.views import login_view, logout_view

urlpatterns = [
    path('admin', admin.site.urls),

    path('api/conf/', include('rest_framework.urls')),
    path('api/geral/', include('common.urls')),
    path('api/medicina/', include('medicina.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('login', login_view),
    path('logout', logout_view),
]
