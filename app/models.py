from django.db import models

# Create your models here.

class Kayit(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="kayit/", default="avatar.png")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Kayitlar"