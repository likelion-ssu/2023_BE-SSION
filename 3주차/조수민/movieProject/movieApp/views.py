
from django.http import JsonResponse
from movieApp.models import Movie
from movieApp.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 


@api_view()
def movie_list(request, id=1):
    movies = Movie.objects.all(id=1)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)





# def movie_list(request):
#     movies = Movie.objects.all()
#     data= {
#         'movies' : list(movies.values())
#     }

#     return JsonResponse(data)

# Create your views here.
