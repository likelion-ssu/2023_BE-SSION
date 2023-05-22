from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=50)
    description=serializers.CharField(max_length=200)
    active=serializers.BooleanField(default=True)