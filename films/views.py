from typing import Any
from django.db.models import Count, Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required, permission_required
from .models import Admin, Film, Genre

from django.contrib.auth import authenticate, login
from django.contrib import messages
from .backend import CustomBackend, is_admin_user
#from django.views.generic import ListView, DetailView
#from .models import Film, Tag

# Create your views here.

def home(request):
    query = request.GET.get('q')
    genres = Genre.objects.all()
    selected_genres = request.GET.getlist('genres')
    films = Film.objects.all().order_by('id')

    if selected_genres:
        # Annotate each film with the number of selected topics it contains
        films = films.annotate(num_genres=Count('genres', filter=Q(genres__in=selected_genres))) \
                     .filter(num_genres=len(selected_genres))

    if query:
        films = films.filter(Q(title__icontains=query))

    films_count = films.count()

    page = request.GET.get('page', 1)
    items_per_page = 8  
    paginator = Paginator(films, items_per_page)

    try:
        url_data = paginator.page(page)
    except PageNotAnInteger:
        url_data = paginator.page(1)
    except EmptyPage:
        url_data = paginator.page(paginator.num_pages)

    context = {
        'url_data': url_data, 
        'films': films[items_per_page * (int(page) - 1): items_per_page * int(page)],
        'query' : query,
        'films_count' : films_count,
        'genres' : genres,
        'selected_genres' : selected_genres,
    }
    return render(request, 'film_list.html', context)


def film_detail(request, id):
    film = get_object_or_404(Film, id=id)
    genres = Genre.objects.all()
    return render(request, 'film_detail.html', {'film': film, 'genres': genres,})


# def admin_login(request):
#     Errors = []
#     mydictionary = {
#         "error" : False,
#         "errors" : Errors
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = CustomBackend.authenticate(request, username=username, password=password)
#         if is_admin_user(user):  # Check if user is admin
#             login(request, user)
#             request.session['deletable_by_admin'] = True
#             messages.success(request, 'You have successfully logged in as admin.')
#             return redirect('manage/')
#         else:
#             error_message = "Invalid username or password!"
#             Errors.append(error_message)
#             mydictionary["error"] = True
#             mydictionary["errors"] = Errors
#             return render(request, 'LifeStyleMag-1.0.0/admin_login.html', context = mydictionary)
#     return render(request, 'LifeStyleMag-1.0.0/admin_login.html')


# def remove_video(request):
#     if request.method == 'POST':
#         video_id = request.POST.get('video_id')
#         video = Video.objects.get(id=video_id)
#         video.delete()
#         return redirect('admin_view')
#     else:
#         return HttpResponse(status=405)
    
# def add_video(request):
#     if request.method == 'POST':
#         form = Video(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_view')
#     else:
#         form = Video()
#     return render(request, 'LifeStyleMag-1.0.0/add_video.html', {'form': form})

# def admin_view(request):
#     # Your existing code from my_view
#     videos = Video.objects.all()
#     page = request.GET.get('page', 1)
#     items_per_page = 8
#     paginator = Paginator(videos, items_per_page)

#     try:
#         url_data = paginator.page(page)
#     except PageNotAnInteger:
#         url_data = paginator.page(1)
#     except EmptyPage:
#         url_data = paginator.page(paginator.num_pages)

#     context = {
#         'url_data': url_data,
#         'videos': videos[items_per_page * (int(page) - 1): items_per_page * int(page)],
#     }

#     return render(request, 'LifeStyleMag-1.0.0/admin_manage.html', context)