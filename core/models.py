from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.email


class Section(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="articles"
    )

    def __str__(self):
        return self.title
