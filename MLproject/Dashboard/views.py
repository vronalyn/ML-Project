from django.shortcuts import render
from .models import WaterQuality

# Create your views here.

def home(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

def predictions(request):
    # Fetch all WaterQuality objects from the database
    water_quality_data = WaterQuality.objects.all()

    # Pass the data to the template context
    context = {'water_quality_data': water_quality_data}
    return render(request, 'dashboard/prediction.html', context)

def input(request):
    context = {}
    return render(request, 'dashboard/predict.html', context)

