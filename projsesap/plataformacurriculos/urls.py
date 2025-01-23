from django.urls import path
from . import views
app_name = 'plataformacurriculos'

urlpatterns = [
    path('', views.index, name='index'),
]