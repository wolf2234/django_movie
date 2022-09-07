from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import *
from .serializers import *
from .service import *
from rest_framework import generics, permissions, viewsets

# Create your views here.


class MovieViewSet(viewsets.ReadOnlyModelViewSet):

    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = PaginationMovies

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):

    serializer_class = ReviewCreateSerializer


class AddStarRatingViewSet(viewsets.ModelViewSet):

    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSerializer
        elif self.action == "retrieve":
            return ActorDetailSerializer


################################################################################
# class MovieListView(ListAPIView):
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = MovieFilter
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=models.Count("ratings",
#                                      filter=models.Q(ratings__ip=get_client_ip(self.request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         return movies
#
#
# class MovieDetailView(RetrieveAPIView):
#     queryset = Movie.objects.filter(draft=False)
#     serializer_class = MovieDetailSerializer
#
#
# class ReviewCreateView(CreateAPIView):
#     serializer_class = ReviewCreateSerializer
#
#
# class AddStarRatingView(CreateAPIView):
#     serializer_class = CreateRatingSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))




#############################################################################
# class MovieListView(APIView):
#
#     def get(self, request):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data)


# class MovieDetailView(APIView):
#
#     def get(self, request, pk):
#         movie = Movie.objects.get(id=pk, draft=False)
#         serializer = MovieDetailSerializer(movie)
#         return Response(serializer.data)


# class ReviewCreateView(APIView):
#
#     def post(self, request):
#         review = ReviewCreateSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)


# class AddStarRatingView(APIView):
#
#     def post(self, request):
#         serializer = CreateRatingSerializer(data=request.data)
#         if serializer.is_valid():
#             print(request.data)
#             serializer.save(ip=get_client_ip(request))
#             return Response(status=201)
#         else:
#             return Response(status=400)


class ActorsListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorsDetailView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

