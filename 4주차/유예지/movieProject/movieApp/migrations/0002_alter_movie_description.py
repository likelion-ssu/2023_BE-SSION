# Generated by Django 4.1 on 2023-05-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]
