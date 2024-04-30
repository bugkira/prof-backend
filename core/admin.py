from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from .models import Article, ContactInfo, Section

# Зарегистрируйте Section с поддержкой MPTT для иерархической структуры
# @admin.register(Section)
# class SectionAdmin(MPTTModelAdmin):
#     list_display = ("name", "parent")
#     ordering = ("name",)
admin.site.register(Section, DraggableMPTTAdmin)
admin.site.register(ContactInfo, admin.ModelAdmin)


# Зарегистрируйте Article для возможности добавления через админку
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "section")
    search_fields = ("title", "content")
