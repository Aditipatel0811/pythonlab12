from django.contrib import admin
from django.urls import path,include
from Aditi_App import views

urlpatterns = [
    path('',views.index)
]
