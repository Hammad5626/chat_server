from django.urls import path
from . import views
app_name = 'chatapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:room_name>/', views.roomName, name='room'),
    path('media/', views.save_media, name='save_media'),
]