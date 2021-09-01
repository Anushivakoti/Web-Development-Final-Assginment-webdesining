from django.shortcuts import render, redirect
from .forms import CatagoeryForm, MealsForm
from django.contrib import messages

from .models import Catagoery, Meals

def homepage(request):
    return render(request, 'meals/homepage.html')



def catagoery_form(request):
    if request.method == "POST":
        form = CatagoeryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Catagoery added successfully')
            return redirect("/meals/get_catagoery")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add catagoery')
            return render(request, 'meals/catagoery_form.html', {'catagoery_form': form})


    context ={
        'catagoery_form': CatagoeryForm,
        'activate_catagoery': 'active'

    }
    return render(request, 'meals/catagoery_form.html', context)

def get_catagoery(request):
    categories =  Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_catagoery':'active'
    }
    return render(request, 'meals/get_catagoery.html', context)

def delete_catagoery(request, catagoery_id):
    catagoery = Catagoery.objects.get(id=catagoery_id)
    catagoery.delete()
    messages.add_message(request, messages.SUCCESS, 'Catagoery Deleted Successfully')
    return redirect('/meals/get_catagoery')




