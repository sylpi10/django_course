from devices import views
from django.urls import path

from devices import views as device_view

urlpatterns = [
    path('add/<str:os>/<str:model>/', device_view.device_add),
    path('all', device_view.all),
    path('<int:id>/', device_view.device_detail),
    path('filter/<str:os>/', device_view.device_filter),
]