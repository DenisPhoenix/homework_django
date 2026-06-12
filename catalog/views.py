from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    if request.method == "GET":
        return render(request, "catalog/home.html")
    return None


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Ответ получен {name}")
    return render(request, "catalog/contacts.html")


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)
