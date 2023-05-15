# Generated by Django 4.2.1 on 2023-05-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('salary', models.IntegerField()),
                ('email', models.CharField(max_length=35)),
            ],
        ),
    ]
