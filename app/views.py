from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import *
from .forms import AutoCreationForm, WorkerCreationForm
# Create your views here.

class AutoView(ListView):
    model = Auto
    template_name = "patp/index.html"
    context_object_name = 'transports'
    


# def index(request):

#     # from django.core import serializers
#     # data = serializers.serialize("python",Avto.objects.all())
#     data = Avto.objects.all()
#     context = {'data':data}
   

#     return render(request, 'patp/index.html', context=context)

def add_auto(request):
    if request.method == 'POST':
        auto_form = AutoCreationForm(request.POST)
        if auto_form.is_valid():
            auto_form.save()
            # return render(request, /,)
    else:
        auto_form = AutoCreationForm()
    return render(request, 'patp/auto_creation.html', {'auto_form':auto_form})

def add_worker(request):
    if request.method == 'POST':
        worker_form = WorkerCreationForm(request.POST)
        if worker_form.is_valid():
            worker_form.save()
            # return redirect
    else:
        worker_form = WorkerCreationForm()
    return render(request, 'patp/worker_creation.html', {'worker_form':worker_form})

# def auto_detail(request, id):
#     pass

def worker_detail(request, worker_id):
    worker = get_object_or_404(Employee,id=worker_id)
    return render(request, 'patp/worker_detail.html', {'worker':worker})



 