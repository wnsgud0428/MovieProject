from django.shortcuts import render
from django.views.generic import FormView, ListView
from . import forms
from django.shortcuts import render, redirect, reverse
# Create your views here.

class MovieEvalView(FormView):
    template_name = "movie/movie_eval.html"
    form_class = forms.MovieEvalForm

    def post(self, request):
        actionScore = request.POST.get("actionScore")
        print(actionScore)
        return redirect(reverse("movies:evaluate-form"))

