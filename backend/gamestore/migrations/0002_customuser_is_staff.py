# Generated by Django 3.2.2 on 2022-02-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
