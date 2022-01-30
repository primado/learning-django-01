from django.shortcuts import render
from django.http import Http404

from .models import *

# Create your views here.
def home(request):
   pets = Pet.objects.all()
   return render(request, 'adoptions/home.html', {'pets': pets})

def  pet_detail(request, pk):
    try:
        pet = Pet.objects.get(id=pk)
    except Pet.DoesNotExist:
        raise Http404("Pet does not exist.")
        
    return render(request, 'adoptions/detail.html', {'pet': pet})