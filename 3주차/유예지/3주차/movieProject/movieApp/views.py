from rest_framework.response import Response
from rest_framework.decorators import api_view
from movieApp.models import Movie
from movieApp.serializers import MovieSerializer
# Create your views here.

@api_view()#어떤 요청 받을 지 명시: default :GET
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET']) #id와 같은 추가적 인자 사용하는 경우 해당 인자 명시적으로 지정해야함
def movie_details(request,id):
    movie=Movie.objects.get(id=id)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)