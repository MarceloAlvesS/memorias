from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='diario'),
    path('<int:pagina_id>/', views.pagina, name='pagina')
]
