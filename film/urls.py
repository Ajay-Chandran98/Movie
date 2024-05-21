# film/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'film'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('command_movie/<int:movie_id>/', views.command_movie, name='command_movie'),
    path('rate_movie/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('add_to_list/<int:movie_id>/', views.add_to_list, name='add_to_list'),
    path('my-list/', views.my_list, name='my_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('remove_from_list/<int:movie_id>/', views.remove_from_list, name='remove_from_list'),
    path('category/<str:category>/', views.category_movies, name='category_movies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)