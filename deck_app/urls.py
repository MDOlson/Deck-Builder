from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("register", views.register),
    path("login", views.login),
    path("logout", views.logout),
    path("welcome", views.welcome),
    path("pick_mat", views.pick_mat),
    path("submit", views.results),
    path("process", views.process),
    path("locate", views.location),
]