from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app.views import *
from django.views.generic import RedirectView


urlpatterns = [

    url(r'^$', index),
    url(r'^contato.html', contato),
    url(r'^inscricao.html', inscricao),
    url(r'^index.html', index),
    url(r'^admin/', admin.site.urls),
    url(r'^cursos.html', cursos),
    url(r'^eventos.html', eventos),
    url(r'^blog.html', blog)
    
]
