from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from movie.views import search_results_view
urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', search_results_view, name='search_results'),


]
