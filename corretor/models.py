from django.db import models
from django.utils import timezone
# Create your models here.
class Contato(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=12)
    email_field = models.EmailField(max_length=40, blank= True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture= models.ImageField(blank=True, upload_to= 'pictures/%Y/%m/')
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'