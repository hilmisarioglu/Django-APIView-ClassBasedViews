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