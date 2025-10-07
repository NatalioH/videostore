# movies/forms.py
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "movie_title",
            "actor1_name",
            "actor2_name",
            "director_name",
            "movie_genre",
            "release_year",
        ]
        widgets = {
            "movie_title":   forms.TextInput(attrs={"class": "form-control"}),
            "actor1_name":   forms.TextInput(attrs={"class": "form-control"}),
            "actor2_name":   forms.TextInput(attrs={"class": "form-control"}),
            "director_name": forms.TextInput(attrs={"class": "form-control"}),
            "movie_genre":   forms.Select(attrs={"class": "form-select"}),
            "release_year":  forms.NumberInput(attrs={"class": "form-control"}),
        }
