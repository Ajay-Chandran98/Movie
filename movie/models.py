from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    poster = models.ImageField(upload_to='movie_images/')
    trailer_link = models.URLField(null=True, blank=True)
    actors = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username



