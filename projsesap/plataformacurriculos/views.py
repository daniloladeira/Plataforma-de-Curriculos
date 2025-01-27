from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CurriculoForm

# Create your views here.

def curriculo_view(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Currículo enviado com sucesso!')
    else:
        form = CurriculoForm()
    return render(request, 'index.html', {'form': form})