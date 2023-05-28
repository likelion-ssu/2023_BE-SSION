from rest_framework import serializers
from movieApp.models import Movie,Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__" #보여줄 필드 지정 가능
        #exclude=[
        #       'running_time'
        # ] 통해 예외 항목 지정 가능
class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)#read_only=True->읽기만 가능_수정 불가
#     title=serializers.CharField(max_length=50)
#     description=serializers.CharField(max_length=150)
#     running_time=serializers.IntegerField()
#     active=serializers.BooleanField()

#     def create(self, validated_data): #save()호출 시 내부적 creat()메서드 호출->정의 필요
#         return Movie.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         #수정하는 로직
#         instance.title=validated_data.get('title',instance.title)#없으면 기본 설정값 이용하라
#         instance.description=validated_data.get('description',instance.description)
#         instance.running_time=validated_data.get('running_time',instance.running_time)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    