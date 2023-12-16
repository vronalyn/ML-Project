from django.shortcuts import render
from .models import WaterPotability
import joblib

model_filename = "C:\\Users\\Ronalyn Villamor\\Documents\\VRONALYN\\ITD105\\django\\MLproject\\datasets\\models\\rfmodel.pkl"
loaded_model = joblib.load(model_filename)

dictsqual = {0: "Not potable", 1: "Potable"}


def classifyWater(request):
    
    val_ph = request.GET.get('ph', 0)
    val_hardness = request.GET.get('hardness', 0)
    val_solids= request.GET.get('solids', 0)
    val_chloramines = request.GET.get('chloramines', 0)
    val_sulfate = request.GET.get('sulfate', 0)
    val_conductivity= request.GET.get('conductivity', 0)
    val_organic = request.GET.get('organic_carbon', 0)
    val_trihalomethanes = request.GET.get('trihalomethanes', 0)
    val_turbidity = request.GET.get('turbidity', 0)
    
    ph = float(val_ph)
    hardness = float(val_hardness)
    solids = float(val_solids)
    chloramines = float(val_chloramines)
    sulfate = float(val_sulfate)
    conductivity = float(val_conductivity)
    organic = float(val_organic)
    trihalomethanes = float(val_trihalomethanes)
    turbidity = float(val_turbidity)

    sampletest = [[ph, hardness, solids, chloramines, sulfate, conductivity, organic, trihalomethanes, turbidity]]
    predicted = loaded_model.predict(sampletest)
    predicted = dictsqual[predicted[0]]
    
    WaterPotability.objects.create(
        ph=ph, hardness=hardness, solids=solids, chloramines=chloramines,
        sulfate=sulfate, conductivity=conductivity, organic_carbon=organic,
        trihalomethanes=trihalomethanes, turbidity=turbidity, potability=predicted
    )

    params = {'Category': predicted}
    return render(request, 'Dashboard/predict.html', params)

