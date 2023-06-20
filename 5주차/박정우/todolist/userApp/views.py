from django.shortcuts import render
from userApp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from userApp.models import User
from rest_framework.exceptions import NotFound, ParseError

# Create your views here.
class SignUp(APIView):
    #유저 생성
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "회원가입 요청이 성공적으로 완료되었습니다."
            })
        else:
            return Response(serializer.errors)   
        
class LogIn(APIView):
    #유저를 가져오는 함수
    def get_user(self, username, password):
        try:
            user = User.objects.get(username=username, password=password)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError("username 또는 password가 필요합니다.")
        user = self.get_user(username, password)
        return Response({
            "user_id" : user.id # 유저 식별시 사용될 id 리턴
        })    
