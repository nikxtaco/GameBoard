# Generated by Django 3.2.2 on 2022-02-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0002_customuser_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
    ]
