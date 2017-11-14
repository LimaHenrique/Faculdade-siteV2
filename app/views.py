from django.shortcuts import render

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
    return render(request, "index.html")

def contato(request):
    return render(request, "contato.html" )

def blog(request):
    return render(request, "blog.html" )

def eventos(request):
    return render(request, "eventos.html" )

def cursos(request):
    return render(request, "cursos.html" )    
    
def inscricao(request):
    return render(request, "inscricao.html" )        
