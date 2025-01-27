from django.urls import path
from .views import curriculo_view
from . import views
app_name = 'plataformacurriculos'

urlpatterns = [
    path('', curriculo_view, name='curriculo'),
    path('banco_de_cv/', views.banco_de_cv, name='banco_de_cv'),
]