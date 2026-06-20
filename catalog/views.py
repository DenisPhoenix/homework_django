from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
