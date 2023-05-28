from rest_framework.response import Response
from rest_framework.decorators import api_view
from movieApp.models import Movie,Review
from movieApp.serializers import MovieSerializer,MovieReviewSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class MovieListView(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        print(serializer.data)
        return Response(serializer.data)  
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)#역시리얼라이저
        if serializer.is_valid(): #데이터 유효 시
            serializer.save()#저장하려면 시리얼라이저 정의해줘야함
            return Response(serializer.data)#db에 저장된 내용 파이썬 형태로 저장
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)#400클라이언트 오류 500서버쪽 오류

class MovieDetailView(APIView):
    def get(self,request,id):
        try:
            movie=Movie.objects.get(id=id)#doest exist 오류 잡기
        except Movie.DoesNotExist:
            return Response({'Error':'없는 영화입니다'},status=status.HTTP_204_NO_CONTENT)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,id):
        try:
            movie=Movie.objects.get(id=id)#doest exist 오류 잡기
        except Movie.DoesNotExist:
            return Response({'Error':'없는 영화입니다'},status=status.HTTP_204_NO_CONTENT)
        movie=Movie.objects.get(id=id)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save() #두개의 인자 넘어갈 시 update 넘어감
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            movie=Movie.objects.get(id=id)#doest exist 오류 잡기
        except Movie.DoesNotExist:
            return Response({'Error':'없는 영화입니다'},status=status.HTTP_204_NO_CONTENT)
        movie=Movie.objects.get(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#status import

class MovieReviewListView(APIView):
    def get(self,request,id): #movies/{id}/
        try:
            movie=Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({'ERROR':'없는 영화입니다'},status=status.HTTP_400_BAD_REQUEST)
        reviews=movie.reviews.all()
        serializer=MovieReviewSerializer(reviews,many=True)
        return Response(serializer.data)
    
    def post(self,request,id):
        pass

class MovieReviewDetailView(APIView):
    def get(self,request,id,review_id):
        try:
            movie=Movie.objects.get(id=id)
            review=Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            return Response({'Error':'없는 리뷰입니다'},status=status.HTTP_204_NO_CONTENT)
        serializer=MovieReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self,request,id,review_id):
        pass
    def delete(self,request,id,review_id):
        try:
            movie=Movie.objects.get(id=id)
            review=Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            return Response({'Error':'없는 리뷰입니다'},status=status.HTTP_204_NO_CONTENT)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])#어떤 요청 받을 지 명시: default :GET
# def movie_list(request):
#     if request.method =='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         print(serializer.data)
#         return Response(serializer.data)   
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)#역시리얼라이저
#         if serializer.is_valid(): #데이터 유효 시
#             serializer.save()#데이터 유효 시 de-serialization 해서 DB에 저장
#             return Response(serializer.data)#creat 메서드로부터 받은 데이터 보내줌
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)#400클라이언트 오류 500서버쪽 오류
    

# @api_view(['GET','PUT','DELETE']) #id와 같은 추가적 인자 사용하는 경우_put 요청은 개별 데이터 시에만 넣어주기/ 해당 인자 명시적으로 지정해야함
# def movie_details(request,id):
#     if request.method=="GET":
#         try:
#             movie=Movie.objects.get(id=id)#doest exist 오류 잡기
#         except Movie.DoesNotExist:
#             return Response({'Error':'없는 영화입니다'},status=status.HTTP_204_NO_CONTENT)
#         movie=Movie.objects.get(id=id)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method=="PUT":
#         try:
#             movie=Movie.objects.get(id=id)#doest exist 오류 잡기
#         except Movie.DoesNotExist:
#             return Response({'Error':'없는 영화입니다'},status=status.HTTP_204_NO_CONTENT)
#         movie=Movie.objects.get(id=id)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save() #두개의 인자 넘어갈 시 update 넘어감
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method=='DELETE':
#         try:
#             movie=Movie.objects.get(id=id)#doest exist 오류 잡기
#         except Movie.DoesNotExist:
#             return Response({'Error':'없는 영화입니다'},status=status.HTTP_204_NO_CONTENT)
#         movie=Movie.objects.get(id=id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)#status import