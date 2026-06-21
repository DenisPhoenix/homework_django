from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.BlogListView.as_view(), name="blog_list"),
    path(
        "blog_create/new/", views.BlogCreateView.as_view(), name="blog_create"
    ),
    path(
        "blog_detail/<int:pk>/",
        views.BlogDetailView.as_view(),
        name="blog_detail",
    ),
    path(
        "blog_delete/<int:pk>/",
        views.BlogDeleteView.as_view(),
        name="blog_delete",
    ),
    path(
        "blog_edit/<int:pk>/",
        views.BlogUpdateView.as_view(),
        name="blog_edit",
    ),
]
