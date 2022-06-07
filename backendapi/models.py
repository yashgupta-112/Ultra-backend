from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class plans(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255,unique=True)
    storage = models.CharField(max_length=255)
    traffic = models.CharField(max_length=255)
    media = models.BooleanField()
    price = models.FloatField()
    def __str__(self):
        return self.name

class info(models.Model):
    waiting = models.IntegerField(default=1)
    news = models.CharField(max_length=150)
    reply = models.IntegerField(default=30)
    
class tickets(models.Model):
    user = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    
class service(models.Model):
    user = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    purchase_date = models.DateField(default=datetime.date.today())
    next_duedate = models.DateField(default=datetime.date.today()+ datetime.timedelta(1 * 30))
    def __str__(self):
       return self.user

class addon(models.Model):
    user = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    purchase_date = models.DateField(default=datetime.date.today())
    def __str__(self):
       return self.user