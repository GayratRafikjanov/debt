from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from .serializers import (UserDetailSerializer, UserCreateSerializer,
                          UserUpdateSerializer, UserDeleteSerializer, UserListSerializer)
from .services import create_user, update_user, delete_user
from .selectors import get_user_by_id, get_users_list



""" 
    !!!!TASK!!!!
    1: users/create da hich narsa kemayapti, yoki json formatta keladigan qilish kerek yoki 
        form data formatta keladigan qilib o'zgartirish kere
        required yoki optional input field lar qo`shish kere
        
    2: users/update dayam hich narsa kemayapti
    
    PASSWORD HECH QACHON KORINISHI, KELISHI KERAK EMAS, FROMTGA RESPONSE BO`LISHI KERAK EMAS!!!
    """



class UserListView(APIView):
    @swagger_auto_schema(
        operation_description="Get users list",
        responses={200: UserListSerializer(many=True)}
    )
    def get(self, request):
        users = get_users_list()
        return Response({'users': users}, status=200)



class UserCreateView(APIView):

    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        operation_description="Create a new user"
    )

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(serializer.validated_data)
        return Response(
            {'id': user.id, 'message': 'User created'}, status=201)



class UserDetailView(APIView):

    @swagger_auto_schema(
        operation_description='Get detail user'
    )

    def get(self, requset, user_id):
        user = get_user_by_id(user_id)
        user_detail = serializers.UserDetailSerializer(user)
        if not user:
            return Response( {'error': 'User not found'}, status=404)
        return Response({'User': user_detail.data}, status=200)



class UserUpdateView(APIView):

    @swagger_auto_schema(
        request_body=UserUpdateSerializer,
        operation_description='Update an existing user'
    )

    def put(self, request, user_id):
        serializer = UserUpdateSerializer(instance=user,
                                          data=request.data,
                                          partial=True)
        user = get_user_by_id(user_id)
        if not user:
            return Response({"error": "User not found"}, status=404)
        updated_user = update_user(user, request.data)
        return Response({"id": updated_user.id, "message": "User updated!"}, status=200)



class UserDeleteView(APIView):

    @swagger_auto_schema(
        operation_description='Delete an existing user'
    )

    def delete(self, request, user_id, email):
        user = get_user_by_id(user_id)
        user.email = email
        if not user:
            return Response(
                {'error': 'User not found'}, status=404)
        delete_user(user)
        return Response({'message': 'User deleted'}, status=204)


