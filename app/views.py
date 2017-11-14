from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contato

def index(request):
    context = {
        'title' : 'Titulo do site',
        'header' : 'header do site',
        'footer' : 'Rodape do site' ,
        'conteudo' : 'Aqui ira seu conteudo do site',
        'lista':[
              'Template 1' ,
              'Template 2',
              'Template 3',
              'Template 4',
              'Template 5',
              'Template 6',
              'Template 7',
              'Template 8',
              'Template 9',
        ] 
    }
    return render(request, "templates/index.html")

def contato(request):
    form = Contato()
    context = { "templates/contato.html" : form }
    return render(request, "templates/contato.html" , context)

def blog(request):
    form = Contato()
    context = { "templates/blog.html" : form }
    return render(request, "templates/blog.html" , context)

def eventos(request):
    form = Contato()
    context = { "templates/eventos.html" : form }
    return render(request, "templates/eventos.html" , context)

def cursos(request):
    form = Contato()
    context = { "templates/cursos.html" : form }
    return render(request, "templates/cursos.html" , context)    
    
def inscricao(request):
    form = Contato()
    context = {"templates/inscricao.html" : form }
    return render(request, "templates/inscricao.html" , context)        
