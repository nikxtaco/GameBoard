
# Create your models here.

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=32, unique=True)
    country = models.CharField(max_length=100)
    follows = models.ManyToManyField("self", related_name="users", blank=True, symmetrical=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# class FollowRelationship(models.Model):
#     followed = models.ForeignKey("CustomUser", related_name='followed', on_delete=models.CASCADE)
#     followed_by = models.ForeignKey("CustomUser", related_name='followed_by', on_delete=models.CASCADE)


    # def __str__(self):
    #     return self.id


class Platform(models.Model):
    platform_name = models.CharField(max_length=100, null=True)
    # supported_games = models.CharField(max_length=100, null=True)
    def __str__(self):
	    return self.platform_name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100, null=True)
    # published_games = models.CharField(max_length=100, null=True)

    def __str__(self):
	    return self.publisher_name

class Game(models.Model):
    game_name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=100, null=True)
    rating = models.FloatField()
    image = models.ImageField(upload_to = "images/")
    supported_platforms = models.ManyToManyField(Platform, related_name="supported_games", blank=True)
    user_id = models.ManyToManyField(CustomUser, related_name="games", blank=True)
    publisher_id = models.ForeignKey(Publisher, null=True, on_delete= models.CASCADE)

    def __str__(self):
	    return self.game_name

class Character(models.Model):
    character_name = models.CharField(max_length=100, null=True)
    element = models.CharField(max_length=100, null=True)
    level = models.IntegerField()
    user_id = models.ForeignKey(CustomUser, null=True, on_delete= models.SET_NULL)
    # username = models.CharField(max_length=100, null=True)
    game_id = models.ForeignKey(Game, null=True, on_delete= models.CASCADE)
    # game_name = models.CharField(max_length=100, null=True)

    def __str__(self):
	    return self.character_name