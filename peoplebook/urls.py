from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.users_list),
    path('user/<str:display>/', views.users_list),
    path('user/<str:name>/detail/', views.users_detail, name='peoplebook-users-details'),
]