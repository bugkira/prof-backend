from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r"^(?P<path>.*)/$", views.category_detail, name="category-detail"),
]
