from django.urls import path 
from .views import my_view
from .views import home

urlpatterns = [
    path('', my_view, name = 'my_view'),
    path('home/', home, name='home'),
]