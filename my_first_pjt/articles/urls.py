from django.urls import path
from . import views

urlpatterns = [
    path("", views.articles, name="articles"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("data-throw/", views.data_throw, name="throw"),
    path("data-catch/", views.data_catch, name="catch"),
]