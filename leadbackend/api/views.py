from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers import LeadSerializer
from django.shortcuts import get_object_or_404
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
    
"""
URL: localhost:8000/add/
Method: POST
Body:{num1:100,num2:200}
Response: 300
"""

class AddView(APIView):

    def post(self,request,*args, **kwargs):

        # to retrieve client-side data : request.data

        data = request.data
        
        n1 = data.get('num1')
        n2 = data.get('num2')

        add_sum = int(n1) + int(n2)

        context = {"Output":add_sum}

        return Response(data=context)

class ProductView(APIView):

    def post(self,request,*args, **kwargs):

        data = request.data

        n1 = data.get('num1')
        n2 = data.get('num2')

        product = int(n1) * int(n2)

        context = {"Output":product}

        return Response(data=context)


class BMIView(APIView):

    def post(self,request,*args, **kwargs):

        height = int(request.data.get("height"))
        height_in_meter = height/100

        weight_in_kg = int(request.data.get("weight"))

        bmi = weight_in_kg/(height_in_meter**2)

        context = {"BMI Value":bmi}

        return Response(data=context)
    

#########################################################################
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeadSerializer
from .models import Lead


class LeadListCreateView(APIView):

    serializer_class = LeadSerializer  # Fixed typo: 'serilaizer_class' ➝ 'serializer_class'

    def get(self,request,*args,**kwargs):

        queryset = Lead.objects.all()

        # SERIALIZATION: Converts Python queryset to Python native types (dict, list, etc.) which are then rendered into JSON.
        serializer = self.serializer_class(queryset, many=True)

        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)  # DESERIALIZATION: Incoming JSON ➝ Python native types

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class LeadRetrieveUpdateDeleteView(APIView):

    serializer_class = LeadSerializer

    def get(self,request,*args,**kwargs):

        id = kwargs.get('pk')
        lead_instance = get_object_or_404(Lead,id=id)

        serializer = self.serializer_class(lead_instance,many=False)

        return Response(data=serializer.data)
    
    def put(self,request,*args,**kwargs):

        id = kwargs.get('pk')
        lead_instance = get_object_or_404(Lead,id=id)

        serializer = self.serializer_class(data=request.data,instance=lead_instance)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def delete(self,request,*args,**kwargs):

        id = kwargs.get('pk')

        lead = get_object_or_404(Lead, id=id)
        lead.delete()

        return Response(data={"message":"deleted"})
    
class CourseListView(APIView):

    serializer_class = LeadSerializer

    def get(self,request,*args,**kwargs):

        courses = [val[0] for val in Lead.COURSE_OPTION]

        return Response(data=courses)


