from django.shortcuts import render, HttpResponse
from .models import Kayit
from .serializers import KayitSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class KayitListView(APIView):
    def get(self, request):
        kayits = Kayit.objects.all()
        serializer = KayitSerializer(kayits, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = KayitSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)