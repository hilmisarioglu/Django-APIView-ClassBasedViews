from django.shortcuts import render, HttpResponse , get_object_or_404
from .models import Kayit
from .serializers import KayitSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.generics import GenericAPIView , mixins , ListCreateAPIView , RetrieveUpdateDestroyAPIView

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
            # Veriyi istedigim gibi degistirebilirim Yöntem 1
            # new_serializer_data = list(serializer.data)
            # new_serializer_data.append({"a":"b"})
            # return Response(new_serializer_data)
            # Veriyi istedigim gibi degistirebilirim Yöntem 2
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

# Abstract bir yapiya döner ve bir sürü farkli islem yapilabilir, pagination , queryset i tanimlamamizi sagliyor , lookup_field i tanimlamamizi sagliyor veya filters. Bir de mixings ler var. GenericApiView , ApiViews den inherit ediyor ve mixingslerle kullaniliyor. Birden fazla class inherit eden seylere mixings deniyor. 

class KayitListCreate(mixins.ListModelMixin,mixins.CreateModelMixin, GenericAPIView):
    queryset= Kayit.objects.all()
    serializer_class=KayitSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class KayitRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
################ Concrete View Classes ####################

# En cok tercih edilen views. Override custom bi sey yazacaksak yukaridaki gibi classbasedviews kullanmak gerekiyor. Ama basit islemlerde bunlar tercih edilmeli. Veriyi istedigim gibi degistirmek istiyorsam ApiViews tercih edilebilir.
#Concrete View Classes
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

class KayitConceteListCreate(ListCreateAPIView):
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer

class KayitConceteRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer

