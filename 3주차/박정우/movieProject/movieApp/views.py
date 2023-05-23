from movieApp.models import Movie
from movieApp.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_details(request, id):
    movies = Movie.objects.get(id=id)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)
    

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(list(movies.values()))
#     data = {
#         'movies': list(movies.values())
#     }
#     return JsonResponse(data)
