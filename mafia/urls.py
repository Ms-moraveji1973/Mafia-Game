from django.urls import path 
from .views import mafia , cart
urlpatterns = [
    path('' , mafia , name='mafia'),
    path('carts' , cart , name="cart_mafia")
]
