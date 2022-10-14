from django.db import models

# Create your models here.



class Info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_addresse = models.EmailField()
    phone_number = models.CharField(max_length=24)


    def __str__(self) -> str: return f'{self.first_name} {self.last_name}'