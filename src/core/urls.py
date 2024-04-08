from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.controllers import login_ctrl, index, logout_ctrl, cadastro_usuario_ctrl, visualizar_usuarios_ctrl, delete_usuario_ctrl, reset_password_ctrl,  visualizar_perfil_ctrl

urlpatterns = [
    path('admin', admin.site.urls),
    
    path('login/', login_ctrl, name="login"),
    path('cadastro/', cadastro_usuario_ctrl, name="cadastro"),
    path('visualizar_perfil/<str:usuario_cpf>', visualizar_perfil_ctrl, name='visualizar_perfil'),
    path('resetar_password/<str:usuario_cpf>', reset_password_ctrl, name='resetar_password'),
    path('delete/<str:usuario_cpf>', delete_usuario_ctrl, name="delete"),
    path('visualizar_usuarios', visualizar_usuarios_ctrl, name="visualizar_usuarios"),
    path('logout/', logout_ctrl, name="logout"),

    path('', index, name='index'),
    path('medicina/', include(('medicina.urls','medicina'))),
    path('enfermagem/', include(('enfermagem.urls','enfermagem'))),
    path('comum/', include(('common.urls','comum'))),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
