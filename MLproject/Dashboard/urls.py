from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'dashboard'),
    path('prediction/', views.home, name = 'prediction'),
]