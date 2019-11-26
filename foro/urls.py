from django.conf.urls import url, include
from .views import ForoList, foro_save, foro_vermas
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^listar', views.ForoList.as_view(), name='foro_listar'),
    url(r'^nuevo$', login_required(views.foro_save), name='foro_nuevo'),
    url(r'^vermas/(?P<id_publicacion>\d+)/$', views.foro_vermas, name='foro_vermas')
]