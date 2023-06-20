from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from userApp.models import User
from planApp.models import Plan
from planApp.serializers import PlanSerializer
from rest_framework.exceptions import ParseError, NotFound

class Plans(APIView):
    def get_user(self,username,password):
        try:
            user=User.objects.get(username=username,password=password)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        
    def post(self,request,user_id):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_user(user_id)
            serializer.save(
		            user=user
		        )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def get(self,request,user_id):
        now=timezone.localtime(timezone.now())
        current_month=now.month
        current_day=now.day

        month=request.query_params.get("month",current_month)
        month=int(month)

        day=request.query_params.get("day",current_day)
        day=int(day)

        user=self.get_user(user_id)
        all_plans=Plan.objects.filter(
            date__month=month,
            date__day=day,
            user=user
        )
        serializer= PlanSerializer(
            all_plans,
            many=True,
        )
        return Response(serializer.data)

class PlanDetail(APIView):
    def get_user(self,user_id):
        try:
            user=User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        
    def get_plan(self,plan_id,user):
        try:
            return Plan.objects.get(id=plan_id,user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
        
    def patch(self,request,user_id,plan_id):
        user=self.get_user(user_id)
        plan=self.get_plan(plan_id,user)

        serializer=PlanSerializer(
            plan,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,user_id,plan_id):
        user=self.get_user(user_id)
        plan=self.get_plan(plan_id,user)
        plan.delete()
        return Response(
            {
                "message":"삭제 성공"
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
    #유저 개별 plan 리턴
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
    #패치 요청 처리
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        serializer = PlanSerializer(
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
    #패치 요청 처리
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        serializer =PlanSerializer(
            plan,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)