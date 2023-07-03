from django.contrib import admin
from django.urls import path 
from . import views 
from .views import upload_excel, download_excel 

urlpatterns = [
   path("",views.index,name="index"),
   path('upload/', upload_excel, name='upload'),
    path('download-excel/', views.download_excel, name='download_excel'),
]
