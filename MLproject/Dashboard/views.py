from django.shortcuts import render, redirect, get_object_or_404
from .models import WaterPotability, AdSales
from Dashboard.models import WaterPotability
from django.db.models import Max, Avg
from django.http import JsonResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'dashboard/overview.html', context)

# Data visualization 
def chart_view(request):
    advertising_data = AdSales.objects.all()
    total_records = WaterPotability.objects.count()
    potable_count = WaterPotability.objects.filter(potability='Potable').count()
    not_potable_count = WaterPotability.objects.filter(potability='Not potable').count()

    # Get the maximum value for each feature (excluding 'potability')
    max_values = WaterPotability.objects.aggregate(
        Max('ph'), Max('hardness'), Max('solids'), Max('chloramines'),
        Max('sulfate'), Max('conductivity'), Max('organic_carbon'),
        Max('trihalomethanes'), Max('turbidity')
    )

    # Extract maximum values
    max_values_list = [
        max_values['ph__max'], max_values['hardness__max'], max_values['solids__max'],
        max_values['chloramines__max'], max_values['sulfate__max'], max_values['conductivity__max'],
        max_values['organic_carbon__max'], max_values['trihalomethanes__max'], max_values['turbidity__max']
    ]

    average_tv_budget = AdSales.objects.aggregate(avg_tv=Avg('TV_Ad_Budget'))['avg_tv']
    average_radio_budget = AdSales.objects.aggregate(avg_radio=Avg('Radio_Ad_Budget'))['avg_radio']
    average_newspaper_budget = AdSales.objects.aggregate(avg_newspaper=Avg('Newspaper_Ad_Budget'))['avg_newspaper']

    return render(request, 'dashboard/chart.html', {
        'potable_count': potable_count,
        'not_potable_count': not_potable_count,
        'total_records': total_records,
        'max_values_list': max_values_list,
        'average_tv_budget': average_tv_budget,
        'average_radio_budget': average_radio_budget,
        'average_newspaper_budget': average_newspaper_budget,
    })

def advertising_data_view(request):
    advertising_data = AdSales.objects.all()


    context = {
        'TV': [item.TV_Ad_Budget for item in advertising_data],
        'Radio': [item.Radio_Ad_Budget for item in advertising_data],
        'Newspaper': [item.Newspaper_Ad_Budget for item in advertising_data],
        'Sales': [item.Sales for item in advertising_data],

    }

    return render(request, 'dashboard/chart.html', {'advertising_data': context})

# Datatables
def predictions(request):
    water_quality_data = WaterPotability.objects.order_by('-date')
    ad_sales_data = AdSales.objects.all()

    # Pass the data to the template context
    context = {'water_quality_data': water_quality_data,
               'ad_sales_data': ad_sales_data,}
    
    return render(request, 'dashboard/prediction.html', context)

# Form view (create prediction)
def input(request):
    context = {}
    return render(request, 'dashboard/predict.html', context)

def sales(request):
    context = {}
    return render(request, 'dashboard/predictsales.html', context)

# # Delete record
# def destroy(request, id):
#     record = get_object_or_404(WaterPotability, id=id)

#     record.delete()
#     return JsonResponse({'message': 'Record deleted successfully'})
def destroy(request, model, id):
    if model == 'water':
        record = get_object_or_404(WaterPotability, id=id)
    elif model == 'sales':
        record = get_object_or_404(AdSales, id=id)
    else:
        return JsonResponse({'message': 'Invalid model specified'}, status=400)
    
    record.delete()
    return JsonResponse({'message': 'Record deleted successfully'})