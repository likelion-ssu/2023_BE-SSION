from rest_framework import serializers
from movieApp.models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = [
        #     'title',
        #     'description'
        # ]
        # exclude = [
        #     'running_time',
        #     'active'
        # ]

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=150)
#     running_time = serializers.IntegerField()
#     active = serializers.BooleanField()
    
#     # validated_data: 사용자에게 받은 데이터
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # instance: 이전에 존재하던 데이터
#     def update(self, instance, validated_data):
#         # validated_data.title이 없다면 instance.title을 그대로 사용
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.running_time = validated_data.get('running_time', instance.running_time)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance