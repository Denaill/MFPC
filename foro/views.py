from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Foro
from .forms import ForoForm
from django.views.generic import ListView

# Create your views here.
class ForoList(ListView):
    model = Foro
    template_name = "foro/foro_list.html"
    

def foro_save(request):
    if request.method == 'POST':
        form = ForoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('foro:foro_listar')
    else:
        form = ForoForm()

    return render(request, 'foro/foro_form.html', {'form':form})

def foro_vermas(request, id_publicacion):
    foro = Foro.objects.get(id=id_publicacion)
    if request.method == 'GET':
        form = ForoForm(instance=foro)
    else:
        form = ForoForm(request.POST, instance=foro)
        if form.is_valid():
            form.save()
        return redirect('foro:foro_listar')
    return render(request, 'foro/foro_vermas.html', {'foro':foro})