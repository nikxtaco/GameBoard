from cgitb import lookup
from rest_framework import serializers

from .models import Hero, Platform, Publisher, Game, Character, CustomUser
# , FollowRelationship
# from .fields

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'platform_name')

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'publisher_name')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_name', 'description', 'genre', 'rating', 'image', 'supported_platforms', 'user_id', 'publisher_id')
        extra_kwargs = {'user_id': {'required': False}}
        # depth = 1

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'character_name', 'element', 'level', 'user_id', 'game_id')

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    # friends = FriendSerializer(many = True)
    games = GameSerializer(many=True)
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'country', 'follows', 'games', 'is_active')
        extra_kwargs = {'games': {'required': False}}
        # depth = 1
        

# class FollowRelationship(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Character
#         fields = ('id', 'followed', 'followed_by')


    # is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(default=timezone.now)