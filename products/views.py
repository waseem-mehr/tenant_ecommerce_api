from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


class GetProductsAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            products = Products.objects.all()
            serializer = GetProductsSerializer(products,many=True)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)




class BrandAPI(APIView):

    def get(self,request,id,*args,**kwargs):
        try:
            brand = Brand.objects.get(id=id)
            serializer = BrandSerializer(brand,many=False)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request,*args,**kwargs):
        try:
            serializer = BrandSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"error":False,"data":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id,*args,**kwargs):
        try:
            brand = Brand.objects.get(id=id)
            brand.delete()
            return Response({},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,*args,**kwargs):
        try:
            brand = Brand.objects.get(id=id)
            serializer = BrandSerializer(brand,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"error":False,"data":serializer.data}, status=status.HTTP_200_OK)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    




class CategoreyAPI(APIView):

    def get(self,request,id,*args,**kwargs):
        try:
            cat = Categorey.objects.get(id=id)
            serializer = CategoreySerializer(cat,many=False)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request,*args,**kwargs):
        try:
            serializer = CategoreySerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"error":False,"data":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id,*args,**kwargs):
        try:
            cat = Categorey.objects.get(id=id)
            cat.delete()
            return Response({},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,*args,**kwargs):
        try:
            cat = Categorey.objects.get(id=id)
            serializer = CategoreySerializer(cat,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"error":False,"data":serializer.data}, status=status.HTTP_200_OK)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)





class ProductAPI(APIView):
    
    def post(self,request,*args,**kwargs):
        try:
            serializer = ProductSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"error":False,"data":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id,*args,**kwargs):
        try:
            obj = Products.objects.get(id=id)
            obj.delete()
            return Response({},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,*args,**kwargs):
        try:
            obj = Products.objects.get(id=id)
            serializer = ProductSerializer(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"error":False,"data":serializer.data}, status=status.HTTP_200_OK)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
    


class GetBusinessProductsAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            products = Products.objects.all()
            serializer = GetProductsSerializer(products,many=True)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)
