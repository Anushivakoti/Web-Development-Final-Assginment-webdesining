

from django.urls import path, include

urlpatterns = [
    path('meals/', include('meals.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))
]

