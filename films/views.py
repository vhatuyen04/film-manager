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
         "static/videos/hahaha.mp4",
        "https://www.youtube.com/embed/7xnz43e0ahA",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "static/videos/hahaha.mp4",
        "https://www.youtube.com/embed/Xg3FFi2hLyY&t=2s",
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

    context = {
        'url_data': url_data,
        'url_links': url_links[items_per_page * (int(page) - 1): items_per_page * int(page)],
    }

    return render(request, 'LifeStyleMag-1.0.0/page1.html', context)
