from django.db import models

# Create your models here.
class image(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="home/images", default="")

    def __str__(self):
        return self.name


