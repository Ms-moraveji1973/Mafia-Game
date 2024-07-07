from django.urls import path 
from .views import mafia
urlpatterns = [
    path('' , mafia , name='mafia')
]
