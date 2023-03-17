from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    '''test API view'''
    serializer_class = serializers.HelloSerializer
    def get(self , request, format=None):
        '''return  a list of APIview features'''
        an_apiview = [
            'Uses HTTP method as function (get, put, post), '
            'Is similar to a traditional',
            'gives a control',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello!!', 'anapiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer._validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST,
                            )
        
    def put(self, request, pk=None):
        '''handle update objects'''
        return Response({'method':'PUT'})
    
    def patch(self, request , pk=None):
        '''handle a partial update of an objects'''
        return Response({'methon': 'PATCH'})
    
    def delete(self, request , pk=None):
        '''handle a Deleteof an objects'''
        return Response({'methon': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    '''Test api view set '''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Resurn a hell message'''
        a_viewset = [
            'uses acttoions (list, create, rertrive, update , patial update',
            'automatically maps to urls uring routrs',
            'provide more functionality with less code',
        ]
        return Response ({'message': 'hello', 'a_viewset' : a_viewset})
    
    def create(selft, request):
        '''create new hello message'''
        serializer = selft .serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer._validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        
       
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        '''Handler getting an object by its ids'''
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        '''Handler updating an object'''
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        '''Handler updationg part of object'''
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        '''Handler removing an oject'''
        return Response({'http_method':'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handling and creating profiles'''
    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends= (filters.SearchFilter,)
    search_fields = ('name', 'email',)
