from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movies,Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request):
    movies = Movies.objects.all()
    categories = Category.objects.all()

    context = {
        'movies': movies,
    }
    return render(request, 'index.html', {'movies': movies, 'categories': categories})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                messages.success(request, f'Welcome, {username}! Your account has been created successfully.')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

@login_required
def profile(request):
    # Fetch user details from the database
    user = User.objects.get(username=request.user.username)  # Assuming user is logged in
    context = {'user': user}
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('login')  # Redirect to the login page after saving changes

    return render(request, 'edit_profile.html', {'user': request.user})


def movie_detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    movie.trailer_link = "https://www.youtube.com/watch?v=VIDEO_ID"  # Replace VIDEO_ID with the actual video ID
    return render(request, 'movie.html', {'movie': movie})


def search_results_view(request):
    query = request.GET.get('query')

    # Filter movies based on the search query
    if query:
        movies = Movies.objects.filter(title__icontains=query)
    else:
        # Handle case when the query is empty
        movies = Movies.objects.all()

    # If only one movie matches the search query, redirect to its movie.html page
    if len(movies) == 1:
        return redirect('movie_detail', movie_id=movies[0].id)

    return render(request, 'search_results.html', {'movies': movies})
