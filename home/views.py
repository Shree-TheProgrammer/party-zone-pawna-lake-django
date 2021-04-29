from django.shortcuts import render, HttpResponse
from .models import image, Contact, gal

# Create your views here.

def home(request):
    images = image.objects.all()
    context = {'images': images}
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        content = request.POST['content']

        user = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, city=city, content=content)
        user.save()
    return render(request, "home/contact.html")


def gallery(request):
    gimages = gal.objects.all()
    gal_img = {'gimages': gimages}
    return render(request, "home/gallery.html", gal_img)

