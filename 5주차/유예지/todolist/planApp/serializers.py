from rest_framework import serializers
from planApp.models import Plan

class PlanSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True) #plan에 있는 유저 필드 하나만 가지고 옴
    plan_id=serializers.IntegerField(source='id',read_only=True)

    class Meta:
        model=Plan
        fields=[
            'plan_id',
            'user',
            'date',
            'content',
            'is_checked',
            'emoji',
        ]