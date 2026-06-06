from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    if request.method == "GET":
        return render(request, "catalog/home.html")
    return None


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Ответ получен {name}")
    return render(request, "catalog/contacts.html")
