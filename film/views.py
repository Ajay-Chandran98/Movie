# film/views.py
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movie.models import Movies
from .models import Command, Rating,MovieList
from .form import MovieForm


def index(request):
    movies = Movies.objects.all()
    last_clicked_movie_id = request.session.get('last_clicked_movie_id')
    last_clicked_movie = get_object_or_404(Movies, id=last_clicked_movie_id) if last_clicked_movie_id else None
    context = {
        'movies': movies,
        'last_clicked_movie': last_clicked_movie,
    }
    return render(request, 'index.html', context)
@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    request.session['last_clicked_movie_id'] = movie_id
    comments = movie.commands.all()
    ratings = movie.ratings.all()
    average_rating = ratings.aggregate(Avg('rating'))['rating__avg'] if ratings else None
    user_rating = ratings.filter(user=request.user).first()
    context = {
        'movie': movie,
        'comments': comments,
        'ratings': ratings,
        'average_rating': average_rating,
        'user_rating': user_rating
    }
    return render(request, 'movie.html', context)



@login_required
def command_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movies, pk=movie_id)
        command_text = request.POST.get('comment')
        if command_text:
            Command.objects.create(movie=movie, user=request.user, text=command_text)
            messages.success(request, 'Comment submitted successfully!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('film:movie_detail', movie_id=movie_id)


@login_required
def rate_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movies, pk=movie_id)
        rating_value = request.POST.get('rating')
        if rating_value and rating_value.isdigit() and 1 <= int(rating_value) <= 10:
            existing_rating = Rating.objects.filter(movie=movie, user=request.user).first()
            if existing_rating:
                existing_rating.rating = int(rating_value)
                existing_rating.save()
            else:
                Rating.objects.create(movie=movie, user=request.user, rating=int(rating_value))
            messages.success(request, 'Rating submitted successfully!')
        else:
            messages.error(request, 'Invalid rating. Please provide a rating between 1 and 10.')
    return redirect('film:movie_detail', movie_id=movie_id)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Command, pk=comment_id)
    if comment.user == request.user or request.user.is_staff:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this comment.')
    return redirect('film:movie_detail', movie_id=comment.movie.id)

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('film:index')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


@login_required
def add_to_list(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    movie_list, created = MovieList.objects.get_or_create(user=request.user)
    movie_list.movies.add(movie)
    return redirect('film:my_list')

# film/views.py

@login_required
def my_list(request):
    movie_list, created = MovieList.objects.get_or_create(user=request.user)
    my_list_movies = movie_list.movies.all()
    context = {
        'my_list_movies': my_list_movies,
    }
    return render(request, 'my_list.html', context)

@login_required
def remove_from_list(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    movie_list = get_object_or_404(MovieList, user=request.user)
    movie_list.movies.remove(movie)
    return redirect('film:my_list')

# film/views.py
from django.shortcuts import render, get_object_or_404
from movie.models import Movies, Category

def category_movies(request, category):
    category = get_object_or_404(Category, name=category)
    movies = Movies.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'category_movies.html', {
        'category': category,
        'movies': movies,
        'categories': categories
    })