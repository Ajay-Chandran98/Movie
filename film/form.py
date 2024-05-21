# film/forms.py
from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']
