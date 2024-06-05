from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User

from .serializers import RegistrationSerializer

# Create your views here.
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        user = request.data
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def profile(request, pk):
    user = User.objects.get(pk=pk)
    
    data = {
        'username':user.username,
        'email':user.email,
        'age':user.age,
        'asset':user.asset,
    }
    return Response(data)

@api_view(['PUT'])
def update(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = RegistrationSerializer(instance=user, data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from .serializers import UserSerializer
# from .models import User
# from rest_framework import generics
# # Create your views here.

# # 회원가입
# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer