from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=150)
    description=serializers.CharField(max_length=150)
    active=serializers.BooleanField(default=True)
    running_time=serializers.IntegerField()