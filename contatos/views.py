

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_contatos(request):
    busca = request.GET.get('q')
    contatos = Contato.objects.filter(usuario=request.user)

    if busca:
        contatos = contatos.filter(nome__icontains=busca)

    return render(request, 'contatos/lista.html', {'contatos': contatos})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lista_contatos")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

