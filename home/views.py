from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "home/index.html")
    #return HttpResponse("<h1><img src='https://source.unsplash.com/1600x450/?nature,water'><br><p style='text-align:center;'>This is Home<h1>")

def about(request):
    return HttpResponse("This is about us")

def contact(request):
    return HttpResponse("This is contact")

def gallery(request):
    return HttpResponse("This is gallery")
