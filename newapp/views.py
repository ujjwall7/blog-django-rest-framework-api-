from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


class registeruser(APIView):
    def post(self,request):
        data=request.data
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':404,'Value':data,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()

        user=User.objects.get(username = serializer.data['username'])
        token_obj ,_ = Token.objects.get_or_create(user=user)


        return Response({'status':200,'Value':data,'token':str(token_obj),'message':'Now You Are Register'})













class BlogApi(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


    def get(self,request):
        print(request.user)

        blog=Blog.objects.all()
        print(request.user)
        serializer=BlogSerializer(blog,many=True)
        return Response({'status':200,'Value':serializer.data})

    
    # def post(self,request):
    #     serializer=BlogSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_201_CREATED)


    # def put(self,request,id):
    #     try:
    #         data=request.data
    #         blog=Blog.objects.get(id=id)
    #         serializer=BlogSerializer(blog,data=request.data)
    #         if not serializer.is_valid():
    #             return Response({'status':404,'Value':data,'errors':serializer.errors,'message':'something went wrong'})
    #         serializer.save()
    #         return Response({'status':200,'Value':data,'message':'data is Saved'})
    #     except Exception as e:
    #         return Response({'status':408,'message':'Invalid Id'})


    # def patch(self,request,id,format= None):
    #     data=request.data
    #     blog = Blog.objects.get(id=id)
    #     serializer = BlogSerializer(blog, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save() 
    #         return Response({ 'msg' : 'Partial Data Updated','data':data}) 
    #     return Response (serializer.errors)


    # def delete(self,request,id):
    #     try:
    #         data=request.data
    #         student=Blog.objects.get(id=id)
    #         student.delete()
    #         return Response({'status':205,'Value':data,'message':'data is deleted'})
    #     except Exception as e:
    #         return Response({'status':408,'message':'Invalid Id'})



class blogq(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        # print(request.user)
        user=request.user
        object=Blog.objects.filter(user=user)
        serializer=BlogSerializer(object,many=True)
        return Response({'status':200,'Value':serializer.data})

    def post(self,request):
        user=request.user
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)


    def put(self,request,id):
        try:
            data=request.data
            blog=Blog.objects.get(id=id)
            serializer=BlogSerializer(blog,data=request.data)
            if not serializer.is_valid():
                return Response({'status':404,'Value':data,'errors':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'Value':data,'message':'data is Saved'})
        except Exception as e:
            return Response({'status':408,'message':'Invalid Id'})


    def patch(self,request,id,format= None):
        data=request.data
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({ 'msg' : 'Partial Data Updated','data':data}) 
        return Response (serializer.errors)


    def delete(self,request,id):
        try:
            data=request.data
            student=Blog.objects.get(id=id)
            student.delete()
            return Response({'status':205,'Value':data,'message':'data is deleted'})
        except Exception as e:
            return Response({'status':408,'message':'Invalid Id'})



from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)





from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({'status':205,'message':'you are logged out'})
