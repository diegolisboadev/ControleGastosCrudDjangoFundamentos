from django.shortcuts import render, redirect
from contas.models import Transacao
from django.http import HttpResponse
from .forms import TransacaoForm
import datetime

# Create your views here.
def home(request):
    return render(request, 'contas/home.html', {'nome' : 'Diego'})
    # return HttpResponse('<h1><strong>Contas - Controle Gastos</strong></h1>')

def url(request):
    return HttpResponse(f'<h3>Teste {datetime.datetime.now()}</h3>')

def listagem(request):
    transacoes = Transacao.objects.all() # Retornar todos os itens (objetos) para a lista
    return render(request, 'contas/listagem.html', {'transacoes': transacoes})

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')
    return render(request, 'contas/form.html', {'form': form})

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk) # filter() -> retornar mais de 1 objeto; get() -> retornar somente 1
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    return render(request, 'contas/form.html', {'form': form})

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    if transacao.delete():
        return redirect('listagem')
