# Generated by Django 3.2.2 on 2022-02-23 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0003_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100, null=True)),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
                ('publisher_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.publisher')),
                ('supported_platforms', models.ManyToManyField(to='gamestore.Platform')),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=100, null=True)),
                ('element', models.CharField(max_length=100, null=True)),
                ('level', models.IntegerField()),
                ('game_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.game')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
