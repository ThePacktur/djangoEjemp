from django.shortcuts import render, redirect
from projectDjangoApp.forms import FromProyecto
from projectDjangoApp.models import Proyecto
# Create your views here.

def index(request):
    return render(request, 'projectDjangoApp/index.html')

def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'projectDjangoApp/proyectos.html',data)

def agregarProyecto(request):
    form = FromProyecto()
    if request.method == 'POST':
        form = FromProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'projectDjangoApp/agregarProyecto.html',data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect('/proyectos')

def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = FromProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FromProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'projectDjangoApp/agregarProyecto.html',data)

