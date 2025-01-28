from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curriculo
from .forms import CurriculoForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def curriculo_view(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST, request.FILES)
        if form.is_valid():
            curriculo = form.save(commit=False)
            ip = get_client_ip(request)
            curriculo.ip_envio = ip
            curriculo.save()
            send_email(curriculo)
            return redirect('plataformacurriculos:curriculo')
    else:
        form = CurriculoForm()
    return render(request, 'index.html', {'form': form})

def banco_de_cv(request):
    curriculos = Curriculo.objects.all()
    return render(request, 'banco_de_cv.html', {'curriculos': curriculos})

def send_email(curriculo):
    subject = "Novo Currículo Recebido"
    message = f"""
    Um novo currículo foi enviado por {curriculo.primeironome}.
    
    Detalhes:
    Nome: {curriculo.primeironome}
    Email: {curriculo.email}
    Telefone: {curriculo.mascara_telefone}
    Cargo Desejado: {curriculo.cargodesejado}
    Escolaridade: {curriculo.get_escolaridade_display()}
    Observações: {curriculo.observacoes}
    
    Verifique o sistema para mais informações.
    """.strip()

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['daniloladeira20@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip