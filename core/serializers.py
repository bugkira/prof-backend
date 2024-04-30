from rest_framework import serializers

from .models import Article, Section


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ["id", "name", "parent", "articles"]
