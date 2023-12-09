from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Avtomobile
from .forms import AvtoForm
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


class AvtoListView(ListView):
    model = Avtomobile
    template_name = 'avtos.html'
    context_object_name = 'avtos'

    def get_context_date(self, **kwargs):
        context = super(AvtoListView, self).get_context_data(**kwargs)
        avtos = Avtomobile.objects.all()
        context['avtos'] = avtos
        return context
    
class AvtoDetailView(DetailView):
    model = Avtomobile
    template_name = 'avto.html'
    context_object_name = 'avto'


class AvtoDeleteView(DeleteView):
    model = Avtomobile
    template_name = 'delete.html'
    success_url = reverse_lazy('avtos')

class AvtoCreateView(CreateView):
    model = Avtomobile
    template_name = 'create.html'
    fields = ('model', 'year', 'price', 'color', 'image')
    success_url = reverse_lazy('avtos')

class AvtoUpdateView(UpdateView):

    model = Avtomobile
    template_name = 'update.html'
    context_object_name = 'avto'
    fields = ('model', 'year', 'price', 'color', 'image')

    def get_success_url(self):
        return reverse_lazy('avto', kwargs={'pk': self.object.id})


    # def get_context_date(self, pk, **kwargs):
    #     context = super(Avtomobile, self).get_context_data(**kwargs)
    #     avto = get_object_or_404(Avtomobile, id=pk)
    #     context['avto'] = avto
    #     return context


# class AvtoDetailView(View):
#     def get(self, request, pk):
#         avto = get_object_or_404(Avtomobile, id=pk)
#         return render(request, 'avto.html', {'avto':avto})


# def avtos(request):
#     avtos = Avtomobile.objects.all()
#     return render(request=request, template_name='avtos.html', context={'avtos':avtos})

# def avto(request, pk):
#     avto = get_object_or_404(Avtomobile, id=pk)
#     return render(request=request, template_name='avto.html', context={'avto':avto})

# def avtodelete(request, pk):
#     avto = get_object_or_404(Avtomobile, id=pk)
#     avto.delete()
#     return redirect('/avtos')

# def avtoupdate(request, pk):
#     avto = get_object_or_404(Avtomobile, id=pk)
#     form = AvtoForm(initial={"model":avto.model, "year":avto.year, "price":avto.price, "color":avto.color})

#     if request.method == 'AVTOMOBILE':
#         form = AvtoForm(request.AVTOMOBILE, instance=avto)
#         if form.is_valid():
#             form.save()
#             return redirect('/posts')
#     return render(request, 'update.html', {'form':form})