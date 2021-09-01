from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('catagoery_form', views.catagoery_form),
    path('get_catagoery', views.get_catagoery),
    path('delete_catagoery/<int:catagoery_id>', views.delete_catagoery),




]
