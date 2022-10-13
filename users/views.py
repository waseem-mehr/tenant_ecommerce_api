import imp
import requests
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions
from django.contrib.sites.shortcuts import get_current_site
from tenant.models import Tenant,Domain
import json

USER = get_user_model()


class AuthentificationBackend(ModelBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        if username is None:
            username = kwargs.get(USER.USERNAME_FIELD)

        
        print(username,password)
        users = USER._default_manager.filter(
            Q(username__iexact=username) | Q(email__iexact=username))

        for user in users:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        if not users:
           
            USER().set_password(password)






class GetUserAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            user = USER.objects.get(email=request.user.email)
            serializer = UserSerializer(user,many=False)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)



class GetUserBusinessAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            user = USER.objects.get(email=request.user.email)
            serializer =  UserBusinessSerializer(user,many=False)
            return Response({"error":False,"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":repr(e)},status=status.HTTP_400_BAD_REQUEST)



class SignupView(APIView):
    

    permission_classes=[permissions.AllowAny]
    
    @transaction.atomic()
    def post(self,request,*args,**kwargs):
        
            
        data=request.data
        pk = data.get("id")
        username = data.get("username")
        print(username)
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        business_name=data.get('business_name')
        email=data.get('email')
        mobile_number=data.get('mobile_number')
        password=data.get('password')
        current_site = str(get_current_site(request)).split(":")[0]
        sub_domain = "{}.{}".format(username,current_site)
        print(sub_domain)
        if password:
            user=USER.objects.filter(email=email).exists()
            usrname = USER.objects.filter(username=username).exists()
            if user or usrname:
                res = {
                    'created':False,
                    'message':f'User with this email or username already exists!'
                    }
                return Response(res)
            else:
                if len(password) < 5 :
                    res = {
                    'created':False,
                    'message':'Password is to short!'
                    }
                    return Response(res)
                print('creating',username,pk,email)
                usr=USER.objects.create_user(
                    id = pk,
                    username = username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    business_name=business_name,
                    mobile_number=mobile_number,
                    password=password,
                    )
                
                usr.save()
                tenant = Tenant(
                    schema_name=usr.username,
                    user = usr,
                    is_active = True
                    )
                tenant.save()
                domain = Domain()
                domain.domain = sub_domain
                domain.tenant = tenant
                domain.is_primary = True
                domain.save()
                res = {
                    'created':True,
                    'username':usr.username,
                    'email':usr.email,
                    'password':password,
                    "sub_domain":str(sub_domain),
                    'message':'Account created successfully!'
                }
                return Response(res)    
        else:
            res = {
                    'created':False,
                    'message':'Password not matched!'
                }
            return Response(res)
