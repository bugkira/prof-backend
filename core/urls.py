from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r"^(?P<path>.*)/$", views.category_detail, name="category-detail"),
]

urlpatterns += [
    path(
        "ckeditor5/", include("django_ckeditor_5.urls"), name="ck_editor_5_upload_file"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
