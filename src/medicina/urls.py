from django.urls import path
from .views import *

urlpatterns = [
    # Consulta
    path('consultas/', list_consultas, name='list_consultas'),
    path('consultas/create', create_consulta, name='create_consulta'),
    path('consultas/<int:pk>/', get_consulta, name='get_consulta'),
    
    # Exames
    path('exames/', list_exames, name='list_exames'),
    path('exames/create', create_exame, name='create_exame'),
    path('exames/<int:pk>/', get_exame, name='get_exame'),

    # Prontuario
    path('prontuarios/', list_prontuarios, name='list_prontuarios'),
    path('prontuarios/create', create_prontuario, name='create_prontuario'),
    path('prontuarios/<int:pk>/', get_prontuario, name='get_prontuario'),
    
    # Atestado
    path('atestados/', list_atestados, name='list_atestados'),
    path('atestados/create', create_atestado, name='create_atestado'),
    path('atestados/<int:pk>/', get_atestado, name='get_atestado'),
]
