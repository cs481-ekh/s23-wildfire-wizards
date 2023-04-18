from django.urls import path
from . import views
from .views import csv_upload

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('csv_upload/', views.csv_upload, name='csv_upload'),
]