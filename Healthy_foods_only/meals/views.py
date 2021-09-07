from django.shortcuts import render, redirect
from .forms import CatagoeryForm, MealsForm
from django.contrib import messages

from .models import Catagoery, Meals, Cart

from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os

def homepage(request):
    return render(request, 'meals/homepage.html')

@login_required
@admin_only
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

@login_required
@admin_only
def get_catagoery(request):
    categories =  Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_catagoery':'active'
    }
    return render(request, 'meals/get_catagoery.html', context)


@login_required
@admin_only
def delete_catagoery(request, catagoery_id):
    catagoery = Catagoery.objects.get(id=catagoery_id)
    catagoery.delete()
    messages.add_message(request, messages.SUCCESS, 'Catagoery Deleted Successfully')
    return redirect('/meals/get_catagoery')

def catagoery_update_form(request, catagoery_id):
    catagoery = Catagoery.objects.get(id=catagoery_id)
    if request.method == "POST":
        form = CatagoeryForm(request.POST,instance=catagoery)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Catagoery updated successfully')
            return redirect("/meals/get_catagoery")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update catagoery')
            return render(request, 'meals/catagoery_update_form.html', {'form_catagoery':form})
    context ={
        'form_catagoery': CatagoeryForm(instance=catagoery),
        'activate_catagoery': 'active'
    }
    return render(request, 'meals/catagoery_update_form.html', context)

@login_required
@admin_only
def meals_form(request):
    if request.method == "POST":
        form = MealsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Meals added successfully')
            return redirect("/meals/get_meals")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add meals')
            return render(request, 'meals/meals_form.html', {'meals_form':form})
    context ={
        'meals_form': MealsForm,
        'activate_meals': 'active'
    }
    return render(request, 'meals/meals_form.html', context)

@login_required
@admin_only
def get_meals(request):
    meals =  Meals.objects.all().order_by('-id')
    context = {
        'meals':meals,
        'activate_meals':'active'
    }
    return render(request, 'meals/get_meals.html', context)

@login_required
@admin_only
def delete_meals(request, meals_id):
    meals = Meals.objects.get(id=meals_id)
    os.remove(meals.meals_image.path)
    meals.delete()
    messages.add_message(request, messages.SUCCESS, 'Meals Deleted Successfully')
    return redirect('/meals/get_meals')


@login_required
@admin_only
def meals_update_form(request, meals_id):
    meals = Meals.objects.get(id=meals_id)
    if request.method == "POST":
        if request.FILES.get('meals_image'):
            os.remove(meals.meals_image.path)
        form = meals_form(request.POST, request.FILES, instance=meals)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Meals updated successfully')
            return redirect("/meals/get_meals")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update food')
            return render(request, 'meals/meals_form.html', {'meals_form':form})
    context ={
        'meals_form': meals_form(instance=meals),
        'activate_meals': 'active'
    }
    return render(request, 'meals/meals_update_form.html', context)

def show_categories(request):
    categories = Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_catagoery_user': 'active'
    }
    return render(request, 'meals/show_categories.html', context)

def show_meals(request):
    meals = Meals.objects.all().order_by('-id')
    context = {
        'meals':meals,
        'activate_meals_user': 'active'
    }
    return render(request, 'meals/show_meals.html', context)

def menu(request):
    categories  = Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_menu':'active'
    }
    return render(request, 'meals/menu.html', context)


@login_required
@user_only
def add_to_cart(request, meals_id):
    user = request.user
    meals = Meals.objects.get(id=meals_id)

    check_item_presence = Cart.objects.filter(user=user, meals=meals)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Item is already added.')
        return redirect('/meals/get_meals_user')
    else:
        cart = Cart.objects.create(meals=meals, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Item added to cart')
            return redirect('/meals/mycart')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add item to cart')

@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user= user)
    context = {
        'items':items,
        'activate_my_cart':'active'
    }
    return render(request, 'meals/mycart.html', context)















