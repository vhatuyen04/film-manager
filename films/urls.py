from django.urls import path
from .views import home, film_detail
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', home, name = 'home'),
    path('films/<int:id>/', film_detail, name='film_detail'),
    # path('admin/', admin_login, name= 'admin_login'),
    # path('admin/manage/', my_view, name = 'my_view'),
    # path('admin/manage/remove-video/', remove_video, name='remove_video'),
    # path('admin/manage/add-video/', add_video, name='add_video'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)