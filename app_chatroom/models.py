from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SimpleUser(models.Model):
     name = models.CharField(max_length=200)


class Message(models.Model):
    user = models.ForeignKey(SimpleUser)
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)