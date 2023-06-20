from django.shortcuts import render
from rest_framework.views import APIView
from planApp.models import Plan
from userApp.models import User
from rest_framework.exceptions import NotFound
from django.utils import timezone
from planApp.serializers import PlanSerializer
from rest_framework.response import Response
from rest_framework import status

class Plans(APIView):
    # 개별 유저 받아오기
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user

    # 유저의 모든 일정 받아오기
    def get(self, request, user_id):
        now = timezone.localtime(timezone.now())
        current_month = now.month
        current_day = now.day

        month = request.query_params.get("month", current_month)
        day = request.query_params.get("day", current_day)

        month = int(month)
        day = int(day)

        all_plans = Plan.objects.filter(
            date__month = month,
            date__day = day,
            user = self.get_user(user_id),
        )

        serializer = PlanSerializer(
            all_plans,
            many=True
        )

        return Response(serializer.data)

    # 일정 생성하기
    def post(self, request, user_id):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_user(user_id)
            serializer.save(user=user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PlanDetail(APIView):
    # 개별 유저 받아오기
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user

    # 개별 일정 받아오기
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")

    # 일정 수정하기
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)

        serializer = PlanSerializer(plan, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    # 일정 삭제하기
    def delete(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        plan.delete()
        return Response({
            "message": "삭제 성공"
        }, status=status.HTTP_204_NO_CONTENT)

class PlanCheck(APIView):
    # 개별 유저 받아오기
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user

    # 개별 일정 받아오기
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")

    # 일정 완료로 변경하기
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        serializer = PlanSerializer(plan, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PlanReview(APIView):
    # 개별 유저 받아오기
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user

    # 개별 일정 받아오기
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")

    # 일정에 이모지 추가하기
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        serializer = PlanSerializer(plan, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)