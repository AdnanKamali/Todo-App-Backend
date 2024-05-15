from abc import ABC, abstractmethod
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from constant import http_messages as constants
# Create your views here.

# =========Senario===========
# An user sign up with (username, password)

class SignUpView(ABC):
    @abstractmethod
    def post(self, request):
        '''
            post username and password to sign up
            for continue in todo app
        '''
        pass

class SignUpInformationView(ABC):
    @abstractmethod
    def get(self, request):
        '''
            return user info like first name, last name
        '''
        pass

    @abstractmethod
    def post(self, request):
        '''
            should send me your information like first name and last name
            to complete your information and then use get
        '''
        pass

class SignUpViewImpl(SignUpView, APIView):
    def post(self, request):
        username, password = request.data.get("username"), request.data.get("password")

        if not(username or password):
            return JsonResponse({"message": constants.WRONG_FILED_MESSAGE}, status=404)
        
        user = User(username=username)
        user.set_password(password)
        try:
            user.save()
            return JsonResponse({"message": constants.SIGNUP_SUCCESS_MESSAGE})
        except:
            return JsonResponse({"message": constants.UN_AUTH_MESSAGE}, status=403)
        


class SignUpInformationViewImpl(SignUpInformationView, APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return JsonResponse({"firstName": user.first_name, "lastName":user.last_name})
    
    
    def post(self, request):
        first_name, last_name = request.data.get("firstName"), request.data.get("lastName")

        if not(first_name or last_name):
            return JsonResponse({"message": constants.WRONG_FILED_MESSAGE})
        user = request.user
        try:
            user.first_name = first_name
            user.last_name = last_name

            user.save()
            return JsonResponse({"firstName": first_name, "lastName": last_name})
        except:
            return JsonResponse({"message": constants.SERVER_ERROR}, status=500)
