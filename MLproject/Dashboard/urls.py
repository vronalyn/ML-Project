from django.urls import path
from . import views
from . import potability


urlpatterns = [
    path('', views.home, name = 'dashboard'),
    path('prediction/', views.predictions, name = 'prediction'),
    path('predict/', views.input, name = 'predict'),
    path('classify', potability.classifyWater, name = 'classify'),
    path('delete/<int:id>', views.destroy, name='destroy'),
]