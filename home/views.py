from django.shortcuts import render, HttpResponse, redirect
from .models import image, Contact, gal, keyfeatimg, Post
from django.contrib import messages

# Create your views here.

def home(request):
    images = keyfeatimg.objects.all()
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

        if firstname == '' or lastname == '' or email == '' or phone == '':
            messages.ERROR(request, "Fill your details correctly")
        else:
            user = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, city=city, content=content)
            user.save()
            messages.success(request, "Thank you for contacting us.. we will get you back shortly!!!")
    return render(request, "home/contact.html")


def gallery(request):
    gimages = gal.objects.all()
    gal_img = {'gimages': gimages}
    return render(request, "home/gallery.html", gal_img)

def faq(request):
    return render(request, 'home/faq.html')

def refund(request):
    return render(request, 'home/refund.html')

def termsandcond(request):
    return render(request, 'home/termsandcond.html')

def blog(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'home/blog.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'home/blogPost.html', context)

