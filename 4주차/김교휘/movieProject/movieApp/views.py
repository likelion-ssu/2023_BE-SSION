from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movieApp.models import Movie, Review
from movieApp.serializers import MovieSerializer,ReviewSerializer

class MovieListView(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CreateReview(APIView):
    def post(self, request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class MovieReviewDetailView(APIView):
    def get(self,request, movie_id, review_id):
        try:
            #movie=Movie.objects.get(id=movie_id)
            review=Review.objects.get(movie=movie_id, id=review_id)
        except Review.DoesNotExist:
            return Response({"해당 리뷰가 없습니다"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer=ReviewSerializer(review)
        return Response(serializer.data)
        

    
    def delete(self, request, movie_id, review_id):
        try:
            #movie=Movie.objects.get(id=movie_id)
            review=Review.objects.get(id=review_id, movie=movie_id)
            
        except Review.DoesNotExist:
            return Response({"해당 리뷰가 없습니다"}, status=status.HTTP_400_BAD_REQUEST)
        review.delete()
        return Response(status=status.HTTP_200_OK)