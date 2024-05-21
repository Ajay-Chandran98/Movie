# film/models.py
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from movie.models import Movies  # Ensure this is the correct import path
from django.contrib import admin


class Command(models.Model):
    objects = None
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='commands')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'


class Rating(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.rating}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return self.title


class MovieList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movies)

    def __str__(self):
        return self.user.username + "'s Movie List"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
