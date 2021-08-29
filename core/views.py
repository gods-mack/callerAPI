

from re import T
from django.db import models
from django.db.models.query import RawQuerySet
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import GlobalUser, User, SpamScore
from .serializers import GlobalUserSerializer, UserSerializer

class Register(APIView):
    def get(self, request):
        print (request.__dict__)
        phone = request.query_params.get("phone", None)
        print (phone)
        if phone:
            user = User.objects.get(phone=phone)
        ser = UserSerializer(user)
        return Response(ser.data)

    
    def post(self, request):
        name = request.data.get("name")
        phone = request.data.get("phone")
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        try:
            obj, _ = User.objects.get_or_create(phone=phone)
            obj.phone = phone
            obj.name = name
            if email:
                obj.email = email
            if password is not None:
                obj.password = password
                obj.is_register = True
            obj.save()
        except Exception as e:
            raise e 
        print (name, phone)
        response = {
                'status': 'success',
                "message":"created successfully"
        }
        return Response(response, status=status.HTTP_201_CREATED)

    







class GlobalUserController(APIView):
    def get(self, request):
        search_phone = request.query_params.get("search_phone", None)
        search_name  = request.query_params.get("search_name")
        users = []
        if search_phone:
            try:
                user = User.objects.get(id=search_phone)
                ser  = UserSerializer(user)
                return Response({"result":ser.data})
            except:
                users = GlobalUser.objects.filter(phone=search_phone)
                ser  = GlobalUserSerializer(users, many=True)
                return Response({"result":ser.data})

        elif search_name:
            users = GlobalUser.objects.filter(name__startswith=search_name)
            ser = GlobalUserSerializer(users, many=True)
            return Response({"result":ser.data})
        


    def post(self, request):
        name  = request.data.get("name", "Unknown")
        phone = request.data.get("phone")
        is_spam = request.data.get("is_spam", False)
        if phone:
            obj, _ = GlobalUser.objects.get_or_create(phone=phone,name=name)
            obj.save()
        return Response({"message":"Global entry has been created"})


class SpamController(APIView):
    def post(self, request):
        phone = request.data.get("phone", None)
        is_spam = request.data.get("is_spam", None)
        if is_spam:
            try:
                obj, _ = SpamScore.objects.get_or_create(phone=phone)
                obj.spam_score += 1
                obj.save()
            except Exception as e:
                raise 
        
        return Response({"message":"marked as spam successfully"})  