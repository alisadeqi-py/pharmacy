from urllib import response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import RegistrationSerializer , UserUpdateSerializer , ChangePasswordSerialier , CartSerializers
from ...models import User
from cart.models import Cart
from django.shortcuts import get_object_or_404



class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            User.objects.create_user(username = serializer.data['username'] , 
            email = serializer.data['email'] , address = serializer.data['address'] , password = serializer.data['password'] 
             , first_name = serializer.data['first_name'] , last_name = serializer.data['last_name'] , phonenumber = serializer.data['phonenumber'])
            serializer.save
            data = {
                    'first_name':serializer.validated_data['first_name']
                }
            return Response(data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)



class UserUpdateApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id = request.user.id)
        serializer = UserUpdateSerializer(user)
        return Response(serializer.data) 

    def put(self, request, *args, **kwargs):
        user_r = request.user
        data = request.data
        user = User.objects.get(id = user_r.id)
        user.username = data.get('username')
        user.email = data.get('email')
        user.address = data.get('address')
        user.phonenumber = data.get('phonenumber')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.save()
        return Response('user updated')


class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerialier

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CustomDiscardAuthToken(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    

    def post(self , request):
        request.user.auth_tokekn.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class CartView(generics.GenericAPIView):

    serializer_class = CartSerializers
    permission_classes = [IsAuthenticated]
    def get(self , request , *args, **kwargs):
        #print(request.user.id)
        user = User.objects.get(id = request.user.id)
        carts = get_object_or_404( Cart, user = user)
        serializer = CartSerializers(carts)
        return Response(serializer.data)