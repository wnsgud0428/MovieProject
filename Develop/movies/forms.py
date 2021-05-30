from django import forms  



class MoviePredictForm(forms.Form):
    # 감독, 배우들 , 예산, 장르 , 제작사
    # 배우 최대 3명까지

    director = forms.CharField(label="감독")
    actor1 = forms.CharField(label='배우1')
    actor2 = forms.CharField(label='배우2', required=False)
    actor3 = forms.CharField(label='배우3', required=False)
    genre = forms.CharField(label="장르")
    producer = forms.CharField(label="제작사")
    budget = forms.IntegerField(label="예산")
    
