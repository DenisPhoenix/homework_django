from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.ContactTemplateView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
]
