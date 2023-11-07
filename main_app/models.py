from django.db import models

# Create your models here.
from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# class Finch(models.Model):
#   name = models.CharField(max_length=100)
#   breed = models.CharField(max_length=100)
#   description = models.TextField(max_length=250)
#   age = models.IntegerField()
#   toys = models.ManyToManyField(Toy)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)

#   def __str__(self):
#     return self.name
#   def fed_for_today(self):
#     return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)