from django.shortcuts import render
from rest_framework import generics

from .models import Article, Section
from .serializers import ArticleSerializer, SectionSerializer


class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def home(request):
    return render(request, "base.html")
