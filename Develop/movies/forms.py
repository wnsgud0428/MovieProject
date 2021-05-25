
from django import forms 


class MovieEvalForm(forms.Form):
    
    score = forms.IntegerField(max_value = 5, min_value=1, label="별점")
