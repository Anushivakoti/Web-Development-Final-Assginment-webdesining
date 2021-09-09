from django import forms
from django import forms
from django.forms import ModelForm

from .models import Catagoery, Meals, Order

class CatagoeryForm(ModelForm):
    class Meta:
        model = Catagoery
        fields = "__all__"



class MealsForm(ModelForm):
    class Meta:
        model = Meals
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address', 'payment_method']
