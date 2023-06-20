from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from planApp.models import Plan
from userApp.models import User
from django.utils import timezone
from planApp import serializers
from planApp.serializers import PlanSerializer
from rest_framework import status
# Create your views here.


class Plans(APIView):
    # user_id를 받아 해당 user 리턴
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾지 못했습니다.")
        return user
    
    # get 요청 처리
    def get(self, request, user_id):
        now = timezone.localtime(timezone.now())
        current_month = now.month
        current_day = now.day
        
        month = request.query_params.get("month", current_month)
        month = int(month)
        
        day = request.query_params.get("day", current_day)
        day = int(day)
        
        user = self.get_user(user_id)
        all_plans = Plan.objects.filter(
            date__month = month,
            date__day = day,
            user = user
        )
        serializer = serializer.PlanSerializer(
            all_plans,
            many=True,
        )
        return Response(serializer.data)
    
    def post(self, request, user_id):
        serializer = PlanSerializer(data=request.data)
        if serializers.is_valid():
            user = self.get_user(user_id)
            serializers.save(
                user=user
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class PlanDetail(APIView):
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
        
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        
        serializer = serializers.PlanSerializer(
            plan,
            data=request.data,
            partial=True,
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        plan.delete()
        return Response(
            {
                "message": "삭제 성공"
            },
            status=status.HTTP_204_NO_CONTENT
        )

class PlanCheck(APIView):
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
    
		 
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
    
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        serializer = serializers.PlanSerializer(
            plan,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PlanReview(APIView):
    
		# user_id를 받아 해당 user 리턴
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
    
		# plan_id와 user 객체를 받아 유저가 갖고 있는 개별 plan 리턴
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
    
		# ============= patch 요청 처리 =============
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        serializer = serializers.PlanSerializer(
            plan,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)            