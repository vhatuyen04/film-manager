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
    # Your logic to get the list of URL links
    url_links = [
        "static/videos/hahaha.mp4",
        "https://www.youtube.com/embed/XhW_ZsFZZIk",
        "https://www.youtube.com/embed/mQmFbcFZFhQ",
        "https://www.youtube.com/embed/TAMyLwW9HW8",
        "https://www.youtube.com/embed/zkI0LRK-vEU",
        "https://www.youtube.com/embed/pM3CFiZOU4k",
        "https://www.youtube.com/embed/sEJKG60a1Zc",
        "https://www.youtube.com/embed/YnkgjKI3tR0",
        "https://www.youtube.com/embed/ph2Yw7yeeCw",
        # Add more URLs as needed
    ]

    page = request.GET.get('page', 1)
    items_per_page = 8  # Adjust the number of items per page as needed

    paginator = Paginator(url_links, items_per_page)

    try:
        url_data = paginator.page(page)
    except PageNotAnInteger:
        url_data = paginator.page(1)
    except EmptyPage:
        url_data = paginator.page(paginator.num_pages)
     # Preprocess the list with unique identifiers
    # url_data = [{'url': link, 'id': f'video{index}'} for index, link in enumerate(url_links)]


    context = {
        'url_data': url_data,
        'url_links': url_links,
    }

    return render(request, 'LifeStyleMag-1.0.0/page1.html', context)

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
    url_links = [
        "https://www.youtube.com/embed/ph2Yw7yeeCw",
        # Add more URLs as needed
    ]

     # Preprocess the list with unique identifiers
    url_data = [{'url': link, 'id': f'video{index}'} for index, link in enumerate(url_links)]


    context = {
        'url_data': url_data,
    }

    return render(request, 'LifeStyleMag-1.0.0/page2.html', context)