from rest_framework.decorators import api_view
from rest_framework.response import Response
from movieapp.serializers import MovieSerializer
from movieapp.models import Movie
# Create your views here.
@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    