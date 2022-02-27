from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from gamestore.models import CustomUser
from gamestore.serializers import CustomUserSerializer
from rest_framework.decorators import api_view

# Create your views here.

from rest_framework import viewsets

from .serializers import HeroSerializer, CustomUserSerializer, GameSerializer, PlatformSerializer, PublisherSerializer
from .models import Hero, CustomUser, Game, Platform, Publisher

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = CustomUserSerializer

    @api_view(['GET', 'POST'])
    def user_list(request):
        if request.method == 'GET':
            user = CustomUser.objects.all()
            
            username = request.query_params.get('username', None)
            if username is not None:
                user = user.filter(username__icontains=username)
            
            user_serializer = CustomUserSerializer(user, many=True, context={'request': request})
            return JsonResponse(user_serializer.data, safe=False)
            # 'safe=False' for objects serialization

        elif request.method == 'POST':
            user_data = JSONParser().parse(request)
            user_serializer = CustomUserSerializer(data=user_data, context={'request': request})
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT'])
    def user_details(request, pk):
        try: 
            user = CustomUser.objects.get(pk=pk) 
        except CustomUser.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        if request.method == 'GET': 
            user_serializer = CustomUserSerializer(user, context={'request': request}) 
            return JsonResponse(user_serializer.data) 

        if request.method == 'PUT': 
            user_data = JSONParser().parse(request) 
            user_serializer = CustomUserSerializer(user, data=user_data, context={'request': request}) 
            if user_serializer.is_valid(): 
                user_serializer.save() 
                return JsonResponse(user_serializer.data) 
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer

#     @api_view(['GET', 'POST'])
#     def game_list(request):
#         if request.method == 'GET':
#             game = Game.objects.all()
            
#             game_name = request.query_params.get('game_name', None)
#             if game_name is not None:
#                 user = user.filter(username__icontains=game_name)
            
#             game_serializer = CustomUserSerializer(game, many=True, context={'request': request})
#             return JsonResponse(game_serializer.data, safe=False)
#             # 'safe=False' for objects serialization

#         elif request.method == 'POST':
#             game_data = JSONParser().parse(request)
#             game_serializer = CustomUserSerializer(data=game_data, context={'request': request})
#             if game_serializer.is_valid():
#                 game_serializer.save()
#                 return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED) 
#             return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     @api_view(['GET', 'PUT', 'DELETE'])
#     def game_details(request, pk):
#         try: 
#             game = Game.objects.get(pk=pk) 
#         except Game.DoesNotExist: 
#             return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
#         if request.method == 'GET': 
#             game_serializer = GameSerializer(game, context={'request': request}) 
#             return JsonResponse(game_serializer.data) 

#         elif request.method == 'PUT': 
#             game_data = JSONParser().parse(request) 
#             game_serializer = CustomUserSerializer(game, data=game_data, context={'request': request}) 
#             if game_serializer.is_valid(): 
#                 game_serializer.save() 
#                 return JsonResponse(game_serializer.data) 
#             return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'DELETE': 
#             game.delete() 
#             return JsonResponse({'message': 'Game was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('id')
    serializer_class = PlatformSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('id')
    serializer_class = PublisherSerializer