from django.urls import path

from . import views
from .views import ArticleDetailView, SectionListView

urlpatterns = [
    path("", views.home, name="home"),
    path("sections/", SectionListView.as_view(), name="section-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
]
