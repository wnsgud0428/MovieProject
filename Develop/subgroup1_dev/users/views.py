from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import models
from django.views import View
from users.forms import UserForm


class HomeView(ListView):
    model = models.User
    template_name = "home.html"
    context_object_name = "users"


def index(request):
    """
    login시 쓸 수 있는 module 표시
    """
    return render(request, 'startmodule.html')


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
