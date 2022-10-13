from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

class GetCountriesAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries,many=True)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)


class GetStatesAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            states = State.objects.all()
            serializer = StateSerializer(states,many=True)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)



class GetCitiesAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            cities = City.objects.all()
            serializer = CitySerializer(cities,many=True)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
