from django.urls import path
from . import views, potability, sales

# urls
urlpatterns = [
    path('', views.chart_view, name='chart'),
    path('overview/', views.home, name = 'overview'),
    path('prediction/', views.predictions, name = 'prediction'),
    path('predict/', views.input, name = 'predict'),
    path('predictsales/', sales.predict_sales, name = 'predictsales'),
    path('classify/', potability.classifyWater, name = 'classify'),
    path('delete/<int:id>', views.destroy, name='destroy'),
]