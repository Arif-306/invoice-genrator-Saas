from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
  name = models.CharField(max_length=100)
price = models.DecimalField(max_digits=6, decimal_places=2)
description = models.TextField()
duration_days = models.IntegerField(default=30)


def __str__(self):
   return self.name


class Subscription(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
start_date = models.DateField(auto_now_add=True)
end_date = models.DateField()


def __str__(self):
   return f"{self.user.username} - {self.plan.name}"