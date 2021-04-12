from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.


class HomeView(ListView):
    model = models.User
    template_name = "home.html"
    context_object_name = "users"
