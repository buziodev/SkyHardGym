from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import ClienteForm
from .models import Cliente, Treinador, plano
from django.contrib import messages

def home(request):
    return render(request, 'site_academia/home.html')

def sobre(request):
    return render(request, 'site_academia/sobre.html')

def plano_view(request):
    planos = plano.objects.all()
    return render(request, 'site_academia/plano.html', {'planos': planos})

def contato(request):
    return render(request, 'site_academia/contato.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = ClienteForm()
    
    return render(request, 'site_academia/cadastrar_cliente.html', {'form': form})

def Treinadores_view(request):
    treinadores = Treinador.objects.all()
    return render(request, 'site_academia/treinadores.html', {'treinadores': treinadores})

class CustomLoginView(LoginView):
    template_name = 'site_academia/login.html'

def user_logout(request):
    logout(request)
    return redirect('home')
