from django.db import models
from django.core.validators import *
from django.core import validators

class Catagoery(models.Model):
    catagoery_name = models.CharField(max_length=200, null= True,validators=[validators.MinLengthValidator(2)])
    catagoery_description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.catagoery_name

class Meals(models.Model):
    meals_name = models.CharField(max_length=200)
    meals_name = models.FloatField()
    meals_name = models.FileField(upload_to='static/uploads')
    catagoery = models.ForeignKey(Catagoery,on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.meals_name















