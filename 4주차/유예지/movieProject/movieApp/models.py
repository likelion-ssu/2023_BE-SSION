from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50) #영화제목
    description=models.CharField(max_length=150)#영화설명
    running_time=models.IntegerField()#상영시간
    active=models.BooleanField(default=True)#상영여부
    created_at=models.DateTimeField(auto_now_add=True)#저장 시간 필드 만드는게 좋음
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Review(models.Model): #하나의 영화 여러개의 리뷰 가질 수 있어
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    movie=models.ForeignKey('Movie',on_delete=models.CASCADE,related_name='reviews')#어떻게 접근할건지#movie 모델 삭제되면 review 모델도 따라서 삭제
    created_at=models.DateTimeField(auto_now_add=True)#저장 시간 필드 만드는게 좋음
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.title