

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
