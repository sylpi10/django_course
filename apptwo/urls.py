
from django.contrib import admin
from django.urls import path, register_converter

# from songs import views
from apptwo import views as apptwo_view, converter

register_converter(converter.TwoDigitDays, 'dd')

urlpatterns = [
    path('django/', apptwo_view.hello),
    path('pictures/<str:category>', apptwo_view.pic_detail),
    path('pictures/<str:category>/<int:year>/', apptwo_view.pic_detail),
    path('pictures/<str:category>/<int:year>/<dd:month>', apptwo_view.pic_detail),
]
