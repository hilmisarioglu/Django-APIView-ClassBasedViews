from django.shortcuts import render, HttpResponse , get_object_or_404
from .models import Kayit
from .serializers import KayitSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.generics import GenericAPIView

################## APIView ####################

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
            return Response(serializer.data,  status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class KayitDetailView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Kayit, pk=pk)
    
    def get(self, request,pk):
        kayit = self.get_object(pk)
        serializer = KayitSerializer(kayit)
        return Response(serializer.data)
        
    def put(self, request,pk):
        kayit = self.get_object(pk)
        serializer = KayitSerializer(kayit, data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
# Veriyi istedigim gibi degistirebilirim
            serializer._data["success"] = "Kayit updated..."
            serializer._data["first_name"] = "Veli"
            print(serializer.data)
            return Response(serializer.data )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        kayit = self.get_object(pk)
        kayit.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

################ GenericAPIView ##################
# Genelde generic view veya Concrete view kullanilir. Abstract bir yapiya döner ve bir sürü farkli islem yapilabilir, pagination gibi.

1.14
