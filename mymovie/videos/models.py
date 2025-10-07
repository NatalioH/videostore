
# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

CURRENT_YEAR = datetime.date.today().year

class Movie(models.Model):
    GENRES = [
        ("COMEDY", "Comedy"),
        ("ROMANCE", "Romance"),
        ("ACTION", "Action"),
        ("DRAMA", "Drama"),
        ("HORROR", "Horror"),
        ("SCIFI", "Sci-Fi"),
        ("OTHER", "Other"),
    ]

    movie_id = models.AutoField(primary_key=True)  # unique ID for each movie
    movie_title = models.CharField(max_length=200)
    actor1_name = models.CharField(max_length=120)
    actor2_name = models.CharField(max_length=120, blank=True)
    director_name = models.CharField(max_length=120)
    movie_genre = models.CharField(max_length=12, choices=GENRES, default="OTHER")
    release_year = models.IntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(CURRENT_YEAR+1)]
    )

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"

