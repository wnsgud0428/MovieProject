
from django import forms 
#from django.contrib.postgres.fields import ArrayField

class MovieEvalForm(forms.Form):
    score = forms.IntegerField(max_value = 5, min_value=1, label="별점")
