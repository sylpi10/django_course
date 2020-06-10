from django.contrib import admin
from django.urls import path

from songs import views

urlpatterns = [
    path('all/', views.songs_list),
#     path('form/', views.thanks, name='thanks'),
    path('form/', views.get_form_data, name='get_form_data'),
    path('add/<str:song_name>/<int:duration>/', views.song_add),
]
