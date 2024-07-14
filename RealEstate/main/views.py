from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.

def home_view(request: HttpRequest):
    return render(request, "main/home.html")

def properties_view(request: HttpRequest):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    context = {"properties": properties}
    return render(request, "main/properties.html", context)

def contact_view(request: HttpRequest):
    return render(request, "main/contact.html")

def dark_mode_view(request: HttpRequest):
    response = redirect("RealEstate:home")
    response.set_cookie("mode", "dark", max_age=60*60*24)
    return response

def light_mode_view(request: HttpRequest):
    response = redirect("RealEstate:home")
    response.set_cookie("mode", "dark", max_age=-3600)
    return response
