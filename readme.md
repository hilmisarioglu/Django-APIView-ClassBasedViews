# CRUD
```bash
# CREATING VIRTUAL ENVIRONMENT

# windows
py -m venv env
# windows other option
python -m venv env

# ACTIVATING ENVIRONMENT
# windows
source ./env/Scripts/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
django-admin --version
django-admin startproject main .
```

go to settings.py, make amendments below
```python
from decouple import config
SECRET_KEY = config('SECRET_KEY')
go to terminal
```bash
py manage.py migrate
py manage.py runserver
```
click the link with CTRL key pressed in the terminal and see django rocket.
go to terminal, stop project, add app
```
py manage.py startapp fscohort
```
go to settings.py and add 'fscohort' app to installed apps and add below lines
```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
create these folders at project level as /media/student
go to fscohort/models.py

```python
from django.db import models
# Create your models here.
class Kayit(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="kayit/", default="avatar.png")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```
go to terminal
```bash
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate
```
go to app.admin.py

```python
from django.contrib import admin
from .models import Kayit
# Register your models here.

admin.site.register(Kayit)

go to terminal

```bash
pip install djangorestframework
pip install django-extensions # needed for extra futures such as shell_plus
pip install ipython # for visualization of shell screen
```
go to settings.py and add 'rest_framework' app and 'django_extensions' to installed apps

## Serializers

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

## Declaring Serializers with serializers.Serializer

create serializers.py under app

```python
from rest_framework import serializers
from .models import Kayit

# Böyle de yapilir ama biz genelde daabase deki fieldlere referans yapmaya calisiyoruz. ModelSerializer kullaniyoruz

class KayitSerializerWithSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

```

## ModelSerializer

go to serializers.py and make below amendments

```python
# Artik forms.py a gerek kalmadi serializers var
from rest_framework import serializers
from .models import Kayit

class KayitSerializer(serializers.ModelSerializer):
    class Meta:
# Modelle baglantisini kurduk. Yukaridaki diger örnekte ise modelle bir baglantisi yok. O yüzden o yöntem uzun. 
        model = Kayit
# 3 farkli sekilde fields referans göserilebilir.  
        fields = ["id", "first_name", "last_name", "email", "image"]
        # fields = '__all__'

# Bunun disindaki her seyi ver demek
        # exclude = ['number']
```
go to main.urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]
```

go to app.urls.py

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
```
from django.shortcuts import render, HttpResponse, 
from .models import Kayit

# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

# If you are using VSCode, Ctrl + Shift + P -> Type and select 'Python: Select Interpreter' and enter into your projects virtual environment. This is what worked for me.

# Run in terminal
# pip install django-rest-framework

# API VIEWS
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
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)

# urls.py git
from django.urls import path
from .views import home, KayitListView

urlpatterns = [
    path('', home),
    path('list/', KayitListView.as_view()),
]

# views.py son hali 
from django.shortcuts import render, HttpResponse , get_object_or_404
from .models import Kayit
from .serializers import KayitSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.generics import GenericAPIView , mixins , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action

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

# En cok tercih edilen views bu bir de modelviewsets var. Override custom bi sey yazacaksak yukaridaki gibi classbasedviews kullanmak gerekiyor. Ama basit islemlerde bunlar tercih edilmeli. Veriyi istedigim gibi degistirmek istiyorsam ApiViews tercih edilebilir.
#Concrete View Classes
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

class KayitConceteListCreate(ListCreateAPIView):
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer

class KayitConceteRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer

################ Viewsets ##################

# KayitConceteListCreate ve KayitConceteRetrieveUpdateDelete i ayni view altina koymanin bir yöntemidir. Bunu kullanmak icin routers lari kullanmak gerekir.Bize default routerlar verir. Daha da isimizi kolaylastirir. 

class KayitVSListRetrieve(mixins.ListModelMixin,mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer

# Asagidaki KayitMVS ile get , post , put , delete tüm islemleri tek bir url altinda yapabiliyoruz vr cok basit. Tek yapmak gereken urls e router eklemek. Normalde put islemleri icin urls e pk de yazmak gerekiyordu fakat burda gerek kalmadi, urls e router.register('kayit-mvs', KayitMVS) ifadesini yazmamiz yeterli. kayit-mvs/1 dersek de 1 numarali id ye gider.Yukaridaki KayitVSListRetrieve icine mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,GenericViewSet yazmis olsaydim ayni sey olmus olurdu,
class KayitMVS(ModelViewSet):    
    queryset = Kayit.objects.all()
    serializer_class = KayitSerializer
    
# Alttaki action su ise yarar. kayit-mvs diye endpoint olusturmustuk, bunu yanina / koyup routable urls yazmaya yarar. Eger sayilari ayri bir urlde dönmek istiyorsak bu kullanilir, yani arama cubuguna kayit-mvs/kayit_count yazmamiz yeterli. Mesela Hilmi isminde kac kisi var api olarak döner. Her bir methoda gidip path eklemeye gerek yok kisacasi.

    @action(detail=False , methods=['get'])
    def kayit_count(self, request):
        kayit_count = Kayit.objects.filter(first_name='Hilmi').count()
        count = {
            "Hilmi ismi su kadar " : kayit_count
        }
        return Response(count)
        

# urls.py son hali 
from django.urls import path, include
from .views import (home,
                    KayitListView,
                    KayitDetailView,
                    KayitListCreate , 
                    KayitRetrieveUpdateDelete,KayitConceteListCreate,KayitConceteRetrieveUpdateDelete,KayitVSListRetrieve,
                    KayitMVS
                    )

from rest_framework import routers

router = routers.DefaultRouter()
router.register('kayit-mvs', KayitMVS)
# router.register('kayit-list', KayitVSListRetrieve)


urlpatterns = [
    path('', home),       
    
    # path('list/', KayitListView.as_view()),
    # path('detail/<int:pk>', KayitDetailView.as_view() , name = 'serializer'),
    
    # path('list/', KayitListCreate.as_view()),
    # path('detail/<int:pk>', KayitRetrieveUpdateDelete.as_view() , name = 'serializer'),
    
    # path('list/', KayitConceteListCreate.as_view()),
    # path('detail/<int:pk>', KayitConceteRetrieveUpdateDelete    .as_view() , name = 'serializer'),
    path('', include(router.urls)),
]