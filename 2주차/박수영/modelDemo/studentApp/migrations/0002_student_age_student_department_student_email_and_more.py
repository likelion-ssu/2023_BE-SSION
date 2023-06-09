# Generated by Django 4.2.1 on 2023-05-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('SW', '소프트웨어학부'), ('CS', '컴퓨터학부'), ('EE', '전자정보공학부'), ('GM', '글로벌미디어학부'), ('AI', 'AI 융합학부'), ('MM', '미디어경영학과')], default='SW', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='lion@likelion.org', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='lion', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='studentId',
            field=models.CharField(default='20230000', max_length=20),
        ),
    ]
