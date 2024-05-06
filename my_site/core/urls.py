from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r"^(?P<path>.*)/$", views.category_detail, name="category-detail"),
]

urlpatterns += [
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
