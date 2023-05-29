from rest_framework import serializers
from movieApp.models import Movie, Review

class MovieSerializer(serializers.Serializer):
    class Meta:
        model=Movie
        fields="__all__"

class MovieReviewSerializer(serializers.Serializer):
    class Meta:
        movie=MovieSerializer(read_only=True)
        model=Review
        fields="__all__"