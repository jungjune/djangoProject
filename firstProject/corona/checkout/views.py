from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def second(request):
    pass

def cafe(request):
    return render(request, 'checkout/projemp.html')