from django.urls import path

from .views import (ContactTemplateView, ProductCacheListView, ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductListView, ProductUpdateView)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product_cache/", ProductCacheListView.as_view(), name="product_cache_list"),
    path(
        "product_detail/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "product_create/new/",
        ProductCreateView.as_view(),
        name="product_create",
    ),
    path(
        "product_update/<int:pk>/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product_delete/<int:pk>/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
]
