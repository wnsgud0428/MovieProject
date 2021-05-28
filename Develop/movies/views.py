from django.shortcuts import render
from django.views.generic import FormView, ListView
from . import forms
from . import models
import random
from django.shortcuts import render, redirect, reverse
from evaluates import models as eval_model

# Create your views here.

class HomeView(ListView):
    def get(self, request):
        return render(request, "home.html", {})  
    

class MovieRecView(ListView):
    def get(self, request):
        movie_model = models.MovieModel.objects.all()
        try:
            Eval_model = eval_model.Evaluate.objects.get(user="유호성")
            print(Eval_model.keyword == '')

            eval_keyword_list = []
            if Eval_model.keyword != '':
                eval_keyword_list = Eval_model.keyword.split(' ')

            recommend_list = []

            for rkeyword in eval_keyword_list:
                recommend_list += list(models.MovieModel.objects.filter(keyword__contains = rkeyword))

            return render(request, "movie/movie_rec.html", {"eval": Eval_model, "recommend": recommend_list})
        except:
            random_items = random.sample(list(movie_model),10)
            return render(request, "movie/movie_rec.html", {})

        


class MovieEvalView(FormView):
    template_name = "movie/movie_eval.html"

    #recommended_movie = []

    def evaluator(self, keyword_list, user):
        duplicate_keyword_delete_list = list(set(keyword_list))
        recommended_keyword_list = []

        for keyword in duplicate_keyword_delete_list:
            if keyword_list.count(keyword) >= 3:
                recommended_keyword_list.append(keyword)
        keywordStr = ' '.join(recommended_keyword_list)
  
        recommended_movie_list = []
        for rkeyword in recommended_keyword_list:
            recommended_movie_list += list(models.MovieModel.objects.filter(keyword__contains = rkeyword))


        for i in recommended_movie_list:
            print(i)


        print(type(recommended_movie_list))

        Eval_model, created = eval_model.Evaluate.objects.update_or_create(user=user, defaults={
            "user":user, "keyword": keywordStr
        })
        Eval_model.save()
        

        
    def post(self, request):
        movie_id_list = request.POST.getlist("id")
        score_list = request.POST.getlist("score")
        keyword_list = []
        for i in range(len(score_list)):
            if int(score_list[i]) > 3:
                movie_obj = models.MovieModel.objects.get(id=movie_id_list[i])
                keyword = movie_obj.keyword
               
                for key in keyword.split():
                    keyword_list.append(key)

        print(keyword_list)

        if len(keyword_list) >= 5:
            self.evaluator(keyword_list, "유호성")
        return redirect(reverse("movies:evaluate"))

    def get(self, request):
        form_class = forms.MovieEvalForm
        movie_model = models.MovieModel.objects.all()

        try:
            Eval_model = eval_model.Evaluate.objects.get(user="유호성")
            print(Eval_model.keyword == '')

            eval_keyword_list = []
            if Eval_model.keyword != '':
                eval_keyword_list = Eval_model.keyword.split(' ')

            random_items = random.sample(list(movie_model),10)
            return render(request, "movie/movie_eval.html", {"movies": random_items, "form": form_class, "eval": Eval_model})
        except:
            random_items = random.sample(list(movie_model),10)
            return render(request, "movie/movie_eval.html", {"movies": random_items, "form": form_class})