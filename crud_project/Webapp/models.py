from django.db import models
from django.urls import reverse
# Create your models here.
class company(models.Model):
 company_name=models.CharField(max_length=40)
company_logo=models.CharField(null='True',blank='True')
company_city=models.IntegerField(max_length=40)