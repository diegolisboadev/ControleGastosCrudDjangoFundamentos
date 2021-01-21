from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    return render(request, 'contas/home.html', {'nome' : 'Diego'})
    # return HttpResponse('<h1><strong>Contas - Controle Gastos</strong></h1>')
def url(request):
    return HttpResponse(f'<h3>Teste {datetime.datetime.now()}</h3>')