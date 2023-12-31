from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Memory(models.Model):
  title = models.CharField(max_length=100)
  details = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('memory-detail', kwargs={'pk': self.id})
