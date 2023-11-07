from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Memory(models.Model):
  title = models.CharField(max_length=100)
  details = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title