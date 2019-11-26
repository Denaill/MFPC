from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegistroForm
from django.core.urlresolvers import reverse_lazy
from .models import User
# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuarios/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('shop:product_list')