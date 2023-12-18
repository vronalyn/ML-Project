from django.core.management.base import BaseCommand
import csv
from Dashboard.models import AdSales

class Command(BaseCommand):
    help = 'Import AdSales data from CSV'

    def handle(self, *args, **options):
        file_path = 'datasets/Advertising Budget and Sales.csv' 
        with open(file_path, 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
        
                AdSales.objects.create(
                    TV_Ad_Budget=row['TV_Ad_Budget'],
                    Radio_Ad_Budget=row['Radio_Ad_Budget'],
                    Newspaper_Ad_Budget=row['Newspaper_Ad_Budget'],
                    Sales=row['Sales']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported AdSales data'))
