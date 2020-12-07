from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.InputForm, name = 'inputform' ),
    path('result/', views.Result, name = 'result' ),
]
