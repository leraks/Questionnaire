from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name="main_page"),
    path('solution/<int:pk>/', solution_test, name="solution"),
    path('result/<str:title>/', result, name="result")
]