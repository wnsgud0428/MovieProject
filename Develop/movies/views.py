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
        producer = request.POST.get("producer")
        budget = request.POST.get("budget")
    

        ################
        self.predict()

        ################
        print(director)
        print(actor1)
        print(actor2)
        print(actor3)
        print(genre)
        print(producer)
        print(budget)

        return redirect(reverse("movies:predict"))

    
    def predict(self):
        #do your logic
        # 저장할 정보가 뭔지
        # ex) 스트링, 감독  int 예산 등등
        
        # 감독 배우 장르 예산 제작사는 패스

        # db 불러오기 예시 (1개만 불러오는거)
        # genreDB = models.Genre.objects.get(id=??, name=??)
        # 위에꺼 결과가 여러개면 오류남

        # 예시2 여러개 불러오기
        # genreDB = models.Gentre.objects.filter(id= ?? name="")
        ## 위에껀 해당하는거 전부 불러옴
        ## genreDB[0].name  genreDB[0].weight 같이 접근할 수 있음


        # 문제있으면 연락 ㄱ ㄱ ㄱ ㄲ ㄱ ㄱ ㄱ ㄱ ㄱ ㄱ ㄱ 

        pass
       

