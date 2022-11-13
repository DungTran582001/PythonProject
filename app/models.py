from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null =True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    budget = models.FloatField(default=0, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=300, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.owner.name

class Income(models.Model):
    owner = models.ForeignKey(Member,on_delete=models.CASCADE)
    price = models.FloatField(null = True)
    description = models.CharField(max_length=300, null = True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.owner.name
