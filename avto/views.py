from django.shortcuts import render, get_object_or_404, redirect
from .models import Avtomobile
from .forms import AvtoForm

def avtos(request):
    avtos = Avtomobile.objects.all()
    return render(request=request, template_name='avtos.html', context={'avtos':avtos})

def avto(request, pk):
    avto = get_object_or_404(Avtomobile, id=pk)
    return render(request=request, template_name='avto.html', context={'avto':avto})

def avtodelete(request, pk):
    avto = get_object_or_404(Avtomobile, id=pk)
    avto.delete()
    return redirect('/avtos')

def avtoupdate(request, pk):
    avto = get_object_or_404(Avtomobile, id=pk)
    form = AvtoForm(initial={"model":avto.model, "year":avto.year, "price":avto.price, "color":avto.color})

    if request.method == 'AVTOMOBILE':
        form = AvtoForm(request.AVTOMOBILE, instance=avto)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    return render(request, 'update.html', {'form':form})