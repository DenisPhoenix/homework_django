from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.BlogListView.as_view(), name="home"),
]
