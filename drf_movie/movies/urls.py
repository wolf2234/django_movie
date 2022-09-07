from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = format_suffix_patterns([
    path("movie/", MovieViewSet.as_view({'get': 'list'})),
    path("movie/<int:pk>/", MovieViewSet.as_view({'get': 'retrieve'})),
    path("review/", ReviewCreateViewSet.as_view({'post': 'create'})),
    path("rating/", AddStarRatingViewSet.as_view({'post': 'create'})),
    path('actor/', ActorsViewSet.as_view({'get': 'list'})),
    path('actor/<int:pk>/', ActorsViewSet.as_view({'get': 'retrieve'})),
])

# urlpatterns = [
#     path('movies/', MovieListView.as_view(), name='movies'),
#     path('movie/<int:pk>/', MovieDiew.as_view(), name='movie_detail'),
#     path('review/', ReviewCreateView.as_view(), name='review'),
#     path('rating/', AddStarRatingView.as_view(), name='rating'),
#     path('actors/', ActorsListView.as_view(), name='actors'),
#     path('actors/<int:pk>/', ActorsDetailView.as_view(), name='actor_detail'),
# ]

