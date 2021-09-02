from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('catagoery_form', views.catagoery_form),
    path('get_catagoery', views.get_catagoery),
    path('delete_catagoery/<int:catagoery_id>', views.delete_catagoery),
    path('update_catagoery/<int:catagoery_id>', views.catagoery_update_form),

    path('meals_form', views.meals_form),
    path('get_meals', views.get_meals),
    path('delete_meals/<int:meals_id>', views.delete_meals),
    path('update_meals/<int:meals_id>', views.meals_update_form),


]

