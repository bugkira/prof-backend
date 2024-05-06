from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Article, ContactInfo, Section

admin.site.register(Section, DraggableMPTTAdmin)
admin.site.register(ContactInfo, admin.ModelAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "section")
    search_fields = ("title", "content")
