from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

class Profile(models.Model):
    photo = models.ImageField(upload_to='images/', blank=True)
    bio = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    profile = models.ManyToManyField(Profile)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    # comments = models.ManyToManyField(comments)
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_caption(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)       

    

    @classmethod
    def search_by_caption(cls,search_term):
        gallery = cls.objects.filter(title__icontains=search_term)
        return gallery
class GalleryLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()        
    