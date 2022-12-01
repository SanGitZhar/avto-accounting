from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.list import ListView
from .models import *
# Create your views here.
class AvtoView(ListView):
    model = Avto
    template_name: "index.html"
    context_object_name: 'avto'



def index(request):

    # from django.core import serializers
    # data = serializers.serialize("python",Avto.objects.all())
    data = Avto.objects.all()
    context = {'data':data,}
   

    
    return render(request, 'patp/index.html', context=context)
