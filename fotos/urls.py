from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:foto_id>/', views.mensagem, name='mensagem'),
    path('<int:foto_id>/editar/', views.editar, name='editar')
]