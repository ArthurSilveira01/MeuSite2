from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.contato_lista, name='contato_lista'),
    path('contato/novo/', views.contato_criar, name='contato_criar'),
    path('contato/<int:pk>/', views.contato_detalhe, name='contato_detalhe'),
    path('contato/<int:pk>/editar/', views.contato_editar, name='contato_editar'),
]