from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curriculo
from .forms import CurriculoForm

# Create your views here.

def curriculo_view(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST, request.FILES)
        if form.is_valid():
            curriculo = form.save(commit=False)
            ip = get_client_ip(request)
            curriculo.ip_envio = ip
            curriculo.save()
            return HttpResponse(f'Currículo enviado com sucesso! IP capturado: {ip}')
    else:
        form = CurriculoForm()
    return render(request, 'index.html', {'form': form})

def banco_de_cv(request):
    curriculos = Curriculo.objects.all()
    return render(request, 'banco_de_cv.html', {'curriculos': curriculos})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip