from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("welcome", views.welcome),
    path("m_list", views.m_list),
    path("d_list", views.d_list),
    path("hardware", views.hardware),
]