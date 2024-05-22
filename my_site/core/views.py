import os

from django.http import Http404
from django.shortcuts import render
from rest_framework import generics

from .models import Article, Section
from .serializers import ArticleSerializer, SectionSerializer


def category_detail(request, path):
    path = path.split("/")
    categories = path
    # return render(request, "path.html", context={"path": request})
    if len(path) == 1:
        try:
            node = Section.objects.get(name=categories[0])
            return render(
                request,
                "MainPage/main_page.html",
                context={
                    "description": node.description,
                    "child_categories": node.children.all(),
                    "articles": node.articles.all(),
                },
            )
        except Section.DoesNotExist as Error:
            raise Http404(f"""У нас нет такой секции.""")

    try:
        node = Section.objects.get(name=categories[0])
        for category in categories[1:-1]:
            node = node.children.get(name=category)
    except Section.DoesNotExist as Error:
        raise Http404(f"""У нас нет такой секции.""")

    try:
        node = node.children.get(name=path[-1])
        return render(
            request,
            "MainPage/main_page.html",
            context={
                "description": node.description,
                "child_categories": node.children.all(),
                "articles": node.articles.all(),
            },
        )
    except Section.DoesNotExist as Error:
        pass

    try:
        article = node.articles.get(title=path[-1])
        return render(
            request,
            "MainPage/main_page.html",
            context={
                "description": node.description,
                "child_categories": node.children.all(),
                "articles": node.articles.all(),
                "is_art": True,
                "art": article.text,
            },
        )
    except Article.DoesNotExist as Error:
        pass

    except Section.DoesNotExist as Error:
        raise Http404(f"""Опечатка. У нас нет такой секции или статьи.""")


def home(request):
    return render(request, "MainPage/main_page.html")
