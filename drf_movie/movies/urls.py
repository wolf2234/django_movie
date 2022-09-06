from django.urls import path, include
from .views import *

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/', ReviewCreateView.as_view(), name='review'),
    path('rating/', AddStarRatingView.as_view(), name='rating'),
    path('actors/', ActorsListView.as_view(), name='actors'),
    path('actors/<int:pk>/', ActorsDetailView.as_view(), name='actor_detail'),
]

