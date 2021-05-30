from django.shortcuts import render
from django.views.generic import ListView

class HomeView(ListView):
    def get(self, request):
        return render(request, "home.html", {})
# Create your views here.
