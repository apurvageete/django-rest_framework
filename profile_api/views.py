from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from . import  serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):


    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview= [
            "Uses HTTP methods as function(get,post,patch,delete)",
            "It is similar to a default Django View",
            "Gives you most control over logic "
        ]
        return Response({'message': "Hello!" ,'an_apiview':an_apiview})


    def post(self,request):
         serializer = serializers.HelloSerializers(data=request.data)
         if serializer.is_valid():
             name = serializer.data.get('name')
             message = 'Hello {0}'.format(name)
             return Response({'message': message})
         else:
             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk= None):
        return Response({'method': 'put'})

    def patch(self,request,pk=None):
        return Response({'method': 'patch'})


    def delete(self,request,pk=None):
        return Response({'method': 'delete'})



class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer


    def list(self,request):
        a_viewset = ["uses action list create ,update,partial update",
        "Automatically maps to urls using routers",
        "provides more Funtionality with less code"]
        return Response({'message': a_viewset})

    def create(self,request):
        serializer = serializers.HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    def retrive(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk = None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk = None):
        return Response({'http_method': 'PATCH'})

    def delete(self,request,pk = None):
        return Response({'http_method': 'DELETE'})
