from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("register", views.register),
    path("new_register", views.new_register),
    path("login", views.login),
    path("have_account", views.have_account),
    path("logout", views.logout),
    path("welcome", views.welcome),
    path("pick_mat", views.pick_mat),
    path("submit", views.results),
    path("process", views.process),
    path("locate", views.location),
    path("render_home", views.render_home),
]