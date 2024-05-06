import django.forms as forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Article, ContactInfo, Section

admin.site.register(Section, DraggableMPTTAdmin)
admin.site.register(ContactInfo, admin.ModelAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "section")
    search_fields = ("title", "content")


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget()
    )  # Поле моделей у нас назвается 'content', поэтому оставляем переменную без именений

    class Meta:
        model = Article  # Тут нужно указать название можеди в которой мы будем использовать CKEditor
        fields = "__all__"
