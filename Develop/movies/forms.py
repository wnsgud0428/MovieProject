
from django import forms 


class MovieEvalForm(forms.Form):
    
    actionScore = forms.IntegerField(max_value = 5, min_value=1, label="액션 점수")
    storyScore = forms.IntegerField(max_value=5, min_value=1, label="스토리 점수")