from django.contrib import admin
from django.urls import path

from songs import views

urlpatterns = [
    path('all/', views.songs_list),
    path('add/<str:song_name>/<int:duration>/', views.song_add),
]
