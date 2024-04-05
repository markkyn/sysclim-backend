from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.controllers import login_ctrl, index

urlpatterns = [
    path('admin', admin.site.urls),
    
    path('login/', login_ctrl, name="login"),

    path('', index, name='index'),
    path('medicina/', include(('medicina.urls','medicina'))),
    path('comum/', include(('common.urls','comum'))),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
