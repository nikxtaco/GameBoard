# Generated by Django 3.2.2 on 2022-02-24 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0010_alter_customuser_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='friends',
        ),
    ]
