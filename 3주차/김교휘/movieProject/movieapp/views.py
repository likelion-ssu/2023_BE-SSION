from django.shortcuts import render
from movieapp.models import Movie
from django.http import JsonResponse
from movieapp.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def movies(request):
    movies=Movie.objects.all()
    data={
        'movies':list(movies.values())
    }
    return JsonResponse(data)

def movie_details(request, id):
    movie=Movie.objects.get(id=id)
    print(movie)
@api_view()
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, id):
    movie=Movie.objects.get(id=id)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)