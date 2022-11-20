from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Avto

# Create your views here.
class AvtoView(ListView):
    model = Avto
    template_name: "index.html"
    context_object_name: 'avto'



def index(request):
    return render(request, 'patp/index.html')