from django.shortcuts import render, HttpResponse
from .models import image
# Create your views here.

def home(request):
    images = image.objects.all()
    context = {'images': images}
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")


def gallery(request):
    return render(request, "home/gallery.html")

