from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm
from django.http import HttpResponse

def contato_lista(request):
    contatos = Contato.objects.all().order_by('nome')
    return render(request,
              'agenda/contato_lista.html',
              {'contatos' : contatos})


def contato_lista_http(request):
    return HttpResponse(
        ''' 
            <h1>Lista de contatos</h1>
        ''')



def contato_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_lista')
    else:
        form = ContatoForm()
        return render(request,
                      'agenda/contato_form.html',
                      {'form' : form,
                      'titulo_pagina': 'Adicionar Contatos'})

def contato_detalhe(request, pk):
    contato = get_object_or_404(Contato, pk)

    return render(request, 'agenda/contato_detalhe.html', {'contato' : contato})

def contato_editar(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)

        if form.is_valid():
            form.save()
            return redirect('agenda:contato_detalhe', pk=contato.pk)
    else:
        form = ContatoForm(instace=contato)

    return render(request,
                  'agenda/contato_form.hmtl',
                  {'form' : form, 'contato' : contato, 'titulo_pagina' : 'Editar'})


