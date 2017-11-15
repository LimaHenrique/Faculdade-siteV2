
from django.conf.urls import url
from app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))

urlpatterns = [

    url(r'^$', index),
    url(r'^contato.html', contato),
    url(r'^inscricao.html', inscricao),
    url(r'^index.html', index),
    url(r'^cursos.html', cursos),
    url(r'^eventos.html', eventos),
    url(r'^blog.html', blog)
    
]
