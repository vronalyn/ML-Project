from django.shortcuts import render
from .models import AdSales
import joblib
import pandas as pd

def predict_sales(request):
    if request.method == 'GET':
        model_filename = 'C:\\Users\\Ronalyn Villamor\\Documents\\VRONALYN\\ITD105\\django\\MLproject\\datasets\\models\\gb_regressor.pkl'

        # Load the trained model
        loaded_model = joblib.load(model_filename)

        if all(key in request.GET for key in ['TV_Ad_Budget', 'Radio_Ad_Budget', 'Newspaper_Ad_Budget']):
            TV_Ad = float(request.GET['TV_Ad_Budget'])
            Radio_Ad = float(request.GET['Radio_Ad_Budget'])
            Newspaper_Ad = float(request.GET['Newspaper_Ad_Budget'])

            # Create a DataFrame with user input
            new_data = pd.DataFrame([[TV_Ad, Radio_Ad, Newspaper_Ad]], columns=['TV_Ad_Budget', 'Radio_Ad_Budget', 'Newspaper_Ad_Budget'])

            # Make predictions using the loaded model on the user input
            predicted_sales = loaded_model.predict(new_data)

            # Save input data and predicted sales to the database
            AdSales.objects.create(
                TV_Ad_Budget=TV_Ad,
                Radio_Ad_Budget=Radio_Ad,
                Newspaper_Ad_Budget=Newspaper_Ad,
                Sales=predicted_sales[0]
            )

            # Render a template with predicted sales
            context = {'predicted_sales': predicted_sales[0]}  # Sending the predicted sales to the template
            return render(request, 'Dashboard/predictsales.html', context)
        else:
            # Render the initial form if data is not complete
            return render(request, 'Dashboard/predictsales.html', {})
    else:
        return render(request, 'Dashboard/predictsales.html', {})
