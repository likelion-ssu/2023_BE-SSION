from rest_framework import serializers
from movieapp.models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # exclude = [
        #     'running_time'
        # ]
        fields ="__all__"
class MovieReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=150)
#     active = serializers.BooleanField(default=True)
#     running_time = serializers.IntegerField()

#     def create(self, validation_data):
#         return Movie.objects.create(**validation_data)
    
#     def update(self, instance, validated_data):
#         #수정하는 로직
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.running_time = validated_data.get('running_time',instance.running_time)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance