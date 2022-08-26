from importlib.util import set_loader
from pyexpat import model
from django.db import models
from  django.contrib.auth.models import AbstractUser
from PIL import Image

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class Profile(models.Model):
    class Meta:
        verbose_name = "My Profile"
        verbose_name_plural = "Profile"
    custom_user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(default="arrivals5.png", upload_to="profile")
    bio = models.CharField(max_length=100, default="bio", null=True, blank=True)
    card_number = models.IntegerField(default=2500, null=True,blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    mobile_number = models.IntegerField(default=998931742328, null=True, blank=True)
    facebook = models.CharField(max_length=200,  null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200,  null=True, blank=True)
    snapchat = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200,  null=True, blank=True)

    def __str__(self):
        return self.telegram

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Carousel(models.Model):

    img = models.ImageField()
    slider_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    aboute = models.TextField(max_length=700)
    price = models.IntegerField(default=1)
    old_price = models.IntegerField(default=2)

    def __str__(self):
        return self.title

class Arrival(models.Model):
    arrivals_img = models.ImageField()
    arrivals_title = models.CharField(max_length=200)
    arrivals_price = models.IntegerField(default=10)
    category = models.ForeignKey("Category",blank=True, on_delete=models.CASCADE)

    #asosiy ma`lumotlar uchun
    arrivals_size  = models.CharField(max_length=30)
    arrivals_text = models.TextField(max_length=700)
    
    def __str__(self):
        return self.arrivals_title



class Product(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Blog(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    aboute = models.TextField(max_length=700)

    def __str__(self):
        return self.title



 
class Category(models.Model):
    class Meta:
        verbose_name = 'My Category'
        verbose_name_plural = 'My Categorys bob'
        
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name