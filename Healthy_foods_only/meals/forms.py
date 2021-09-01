from django import forms
from django import forms
from django.forms import ModelForm

from .models import Catagoery, Meals

class CatagoeryForm(ModelForm):
    class Meta:
        model = Catagoery
        fields = "__all__"



class MealsForm(ModelForm):
    class Meta:
        model = Meals
        fields = "__all__"
