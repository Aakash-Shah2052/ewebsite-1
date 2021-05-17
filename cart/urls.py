from django.urls import path
from .views import *
app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<slug>', add-to-cart,name = 'add-to-cart'),

]