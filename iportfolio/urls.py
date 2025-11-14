from django.urls import path
from . import views

urlpatterns = [
    path("", views.base),
    path("", views.portfolio),
    path("", views.service),
    path("", views.starter),
]
