from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',showCalculator,name="showCalculator"),
    path('calculator-cost/',calculate_cost,name = 'calculate_cost')
]