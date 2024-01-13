from django.urls import path 
from .views import my_view
from .views import home
from .views import article_list
from .views import page2

urlpatterns = [
    path('', my_view, name = 'my_view'),
    path('home/', home, name='home'),
    path('articles/', article_list, name='article-list'),
    path('page2', page2, name='page2')
]