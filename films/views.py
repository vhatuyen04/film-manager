from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic import ListView, DetailView
#from .models import Film, Tag


# Create your views here.

def home(request):
    return HttpResponse("Welcome to film website!")

def my_view(request):
    return render(request, 'LifeStyleMag-1.0.0/page1.html')

#def article_list(request):
    #articles = Article.object.all().order_by('-pub_date')
    #return render(request, 'LifeStyleMag-1.0.0/article_list.html', {'articles': articles})

def article_list(request):
    # Fetch articles or adjust this query based on your models
    articles = Article.objects.all()

    # Paginate the articles
    paginator = Paginator(articles, 10)  # 10 articles per page
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    total_pages = paginator.num_pages

    return render(request, 'LifeStyleMag-1.0.0/article_list.html', {'articles': page, 'page_number': page_number, 'total_pages': total_pages})

def page2(request):
    return HttpResponse("Welcome to page 2!")