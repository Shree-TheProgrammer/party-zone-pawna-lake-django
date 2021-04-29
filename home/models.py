from django.db import models

# Create your models here.
class image(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="home/images", default="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    cno = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.firstname + " " + self.phone

class gal(models.Model):
    ino = models.AutoField(primary_key=True)
    iname = models.CharField(max_length=100)
    gimg = models.ImageField(upload_to="home/images", default="")

    def __str__(self):
        return self.iname


