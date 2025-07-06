from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

"""
HTTPRequest
URL: localhost:8000/morning/
Method: GET
Response: Good Morning!
"""

class GoodMorningView(APIView):

    def get(self,request,*args, **kwargs):

        context = {"message":"Good Morning!"} # Python Dictionary

        # Response class converts python native type to json

        return Response(data=context)

class GoodAfternoonView(APIView):

    def get(self,request,*args, **kwargs):

        context = {"message":"Good Afternoon!"} # Python Dictionary

        # Response class converts python native type to json

        return Response(data=context)
    
class GoodAfternoonView(APIView):

    def get(self,request,*args, **kwargs):

        context = {"message":"Good Afternoon!"} # Python Dictionary

        # Response class converts python native type to json

        return Response(data=context)
    
class GoodEveningView(APIView):

    def get(self,request,*args, **kwargs):

        context = {"message":"Good Evening!"} # Python Dictionary

        # Response class converts python native type to json

        return Response(data=context)
    
class GoodNightView(APIView):

    def get(self,request,*args, **kwargs):

        context = {"message":"Good Night!"} # Python Dictionary

        # Response class converts python native type to json

        return Response(data=context)


