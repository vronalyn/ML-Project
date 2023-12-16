from django.core.management.base import BaseCommand
import pandas as pd
from sklearn.impute import KNNImputer
from Dashboard.models import WaterPotability

class Command(BaseCommand):
    help = 'Import water quality data from CSV'

    def handle(self, *args, **options):
        file_path = 'datasets/water_potability.csv'  

       
        data = pd.read_csv(file_path)
        knn_imputer = KNNImputer(n_neighbors=3)
        cols_to_impute = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']

        # Apply imputation
        data[cols_to_impute] = knn_imputer.fit_transform(data[cols_to_impute])

        dict_qual = {0: "Not potable", 1: "Potable"}

        data['potability'] = data['Potability'].map(dict_qual)

        for index, row in data.iterrows():
            WaterPotability.objects.create(
                ph=row['ph'],
                hardness=row['Hardness'],
                solids=row['Solids'],
                chloramines=row['Chloramines'],
                sulfate=row['Sulfate'],
                conductivity=row['Conductivity'],
                organic_carbon=row['Organic_carbon'],
                trihalomethanes=row['Trihalomethanes'],
                turbidity=row['Turbidity'],
                potability=row['potability']
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported water quality data'))
