from firstapp import views
from django.urls import path

urlpatterns=[
    path("",views.index),
    path("second/",views.second)
]

