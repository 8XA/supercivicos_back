from django.urls import path
from reg_empresa import views

urlpatterns = [
    path('empresas/', views.empresas_lista),
]
