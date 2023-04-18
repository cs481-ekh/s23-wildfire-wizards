from django.urls import path, re_path

from . import views

urlpatterns = [
    path('csv_upload/', views.csv_upload, name='csv_upload'),
]