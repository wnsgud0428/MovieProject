from django.shortcuts import render
from django.views.generic import FormView, ListView
from . import forms
from . import models
import random
from django.shortcuts import render, redirect, reverse
# Create your views here.

class MovieEvalView(FormView):
    template_name = "movie/movie_eval.html"
    keyword_list = []
    recommended_movie = []

    def recommender(self):
        duplicate_keyword_delete_list = list(set(self.keyword_list))
        recommended_keyword_list = []

        for keyword in duplicate_keyword_delete_list:
            if self.keyword_list.count(keyword) >= 1:
                recommended_keyword_list.append(keyword)
        recommended_movie_list = models.MovieModel.objects.filter(keyword__in = recommended_keyword_list)

        return recommended_movie_list

        
    def post(self, request):
        movie_id = request.POST.get("id")
        print(movie_id)
        score = request.POST.get("score")
        print(score)

        if int(score) > 3:
            movie_obj = models.MovieModel.objects.get(id=movie_id)
            print(movie_obj)
            self.keyword_list.append(movie_obj.keyword) 
        print(self.keyword_list)

        if len(self.keyword_list) > 5:

            self.recommended_movie = self.recommender()
            print(self.recommended_movie)
        return redirect(reverse("movies:evaluate-form"))

    def get(self, request):
        form_class = forms.MovieEvalForm
        movie_model = models.MovieModel.objects.all()
        random_items = random.sample(list(movie_model),5)
        return render(request, "movie/movie_eval.html", {"movies": random_items, "form": form_class, "recommend": self.recommended_movie})