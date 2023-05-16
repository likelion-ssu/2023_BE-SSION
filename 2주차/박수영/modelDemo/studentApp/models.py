from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Student(models.Model):
    studentId = models.CharField(max_length=20, default='20230000')
    name = models.CharField(max_length=50, default='lion')
    age = models.PositiveSmallIntegerField(default=20)
    email = models.EmailField(max_length=50, default='lion@likelion.org')
    class Department(models.TextChoices):
        SOFTWARE = 'SW', _('소프트웨어학부')
        COMPUTER_SCIENCE = 'CS', _('컴퓨터학부')
        ELECTRONIC_ENGINEERING = 'EE', _('전자정보공학부')
        GLOBAL_MEDIA = 'GM', _('글로벌미디어학부')
        AI_CONVERGENCE = 'AI', _('AI 융합학부')
        MEDIA_MANAGEMENT = 'MM', _('미디어경영학과')
    department = models.CharField(max_length=2, choices=Department.choices, default=Department.SOFTWARE)