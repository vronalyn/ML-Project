from django.shortcuts import render, redirect, get_object_or_404
from .models import WaterPotability
from django.http import JsonResponse
from Dashboard.models import WaterPotability

# Create your views here.

def home(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

def predictions(request):
    water_quality_data = WaterPotability.objects.order_by('-date')

    # Pass the data to the template context
    context = {'water_quality_data': water_quality_data}
    return render(request, 'dashboard/prediction.html', context)

def input(request):
    context = {}
    return render(request, 'dashboard/predict.html', context)

def destroy(request, id):  
    water_potability = get_object_or_404(WaterPotability, id=id)  
    water_potability.delete()  
    return redirect("dashboard/prediction.html")