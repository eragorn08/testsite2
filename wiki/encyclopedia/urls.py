from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry_page, name="entry_page"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random"),
    path("edit/<str:title>", views.edit_page, name="edit_page"),
    path("add",views.add, name="add")
]
