from django.shortcuts import render
from .models import ProductType, Product, Review

# Create your views here.

def index(request):
    return render(request, 'techapp/index.html')

def getTypes(request):
    types_list = ProductType.objects.all()
    context = {'types_list' : types_list}
    return render(request, 'techapp/types.html', context=context)