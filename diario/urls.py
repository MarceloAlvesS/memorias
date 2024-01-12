from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='diario'),
    path('<int:pagina_id>/', views.pagina, name='pagina'),
    path('<int:pagina_id>/editar/', views.editar, name='editar_pagina'),
    path('<int:pagina_id>/deletar/', views.deletar, name='deletar_pagina'),
    path('criar/', views.criar, name='criar_pagina'),
]
