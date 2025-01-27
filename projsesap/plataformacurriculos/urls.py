from django.urls import path
from .views import curriculo_view
app_name = 'plataformacurriculos'

urlpatterns = [
    path('', curriculo_view, name='curriculo'),
]