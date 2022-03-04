from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HomePage(APIView):
    def get(self, format=None):
        massage = "hi"
        return Response(massage)

