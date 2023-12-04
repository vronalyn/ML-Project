from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

def predictions(request):
    context = {}
    return render(request, 'dashboard/result.html', context)

