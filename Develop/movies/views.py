from django.shortcuts import render,redirect, reverse
from django.views.generic import ListView, FormView
from . import forms
from . import models


class HomeView(ListView):
    def get(self, request):
        return render(request, "home.html", {})


class PredictView(FormView):

    def get(self, request):
        form = forms.MoviePredictForm
        return render(request, "predict.html", {"forms": form})

    def post(self, request):

        director = request.POST.get("director")
        actor1 = request.POST.get("actor1")
        actor2 = request.POST.get("actor2")
        actor3 = request.POST.get("actor3")
        
        genre = request.POST.get("genre")
        budget = request.POST.get("budget")

        decision_value = self.predict(director, actor1, actor2, actor3, genre, budget)


        form = forms.MoviePredictForm
        return render(request, "predict_result.html", {"decision_value": decision_value})


    def predict(self, director, actor1, actor2, actor3, genre, budget):

        def weight_func(DB):
            if DB == 'super-hit':
                return 4
            elif DB == 'hit':
                return 3
            elif DB == 'soso':
                return 2
            else:
                return 1

        def budget_func(budget):
            if int(budget) < 0.95:
                return 1
            elif 0.95 <= int(budget) <= 15:
                return 2
            elif 15 < int(budget) <= 40:
                return 3
            else:
                return 4

        def predict_decision(total):
            if total >= 18:
                return 4
            elif 13 <= total < 18:
                return 3
            elif 8 < total < 13:
                return 2
            else:
                return 1

        try:
            genreDB = models.Genre.objects.get(name=genre)
        except models.Genre.DoesNotExist:
            genreDB = None

        try:
            DirectorDB = models.Director.objects.get(name=director)
        except models.Director.DoesNotExist:
            DirectorDB = None
        
        try:
            Actor1DB = models.Actor.objects.get(name=actor1)
        except models.Actor.DoesNotExist:
            Actor1DB = None
        
        try:
            Actor2DB = models.Actor.objects.get(name=actor2)
        except models.Actor.DoesNotExist:
            Actor2DB = None
        
        try:
            Actor3DB = models.Actor.objects.get(name=actor3)
        except models.Actor.DoesNotExist:
            Actor3DB = None
        
        total_weight = 0
        
        if genreDB is not None:
            total_weight += weight_func(genreDB.weight)

        if DirectorDB is not None:
            total_weight += weight_func(DirectorDB.weight)

        if Actor1DB is not None:
            total_weight += weight_func(Actor1DB.weight)


        if Actor2DB is not None:
            total_weight += weight_func(Actor2DB.weight)
        else:
            if Actor1DB is not None:
                total_weight += weight_func(Actor1DB.weight)


        if Actor3DB is not None:
            total_weight += weight_func(Actor3DB.weight)
        else:
            if Actor1DB is not None:
                total_weight += weight_func(Actor1DB.weight)


            
        total_weight += budget_func(budget)
        
        decision_value = predict_decision(total_weight)
        print(total_weight)
        print(decision_value)

        return decision_value

       

