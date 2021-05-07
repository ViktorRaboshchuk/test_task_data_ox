from django.contrib import admin
from django.urls import path, include

from yahoo_data import views

urlpatterns = [
    path("all_data/", views.HistoricalDataList.as_view()),
]
