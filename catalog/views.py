from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.models import Product

from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product/product_list.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "catalog/contacts.html"
