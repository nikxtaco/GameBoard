# Generated by Django 3.2.2 on 2022-02-23 17:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0004_character_game_platform_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
