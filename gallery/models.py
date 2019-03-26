from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    bio = models.CharField(max_length =30)

    def __str__(self):
        return self.bio
class tags(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name 

class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length =30 )
    caption = models.TextField(null = True)
    user = models.ForeignKey(User,null=True)
    # profile = models.ManyToManyField(Profile)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    # comments = models.ManyToManyField(comments)
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
    	self.delete()
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image
    def __str__(self):
    	return self.user.username
   
    @classmethod
    def search_by_name(cls,search_term):
        gallery = cls.objects.filter(name__icontains=search_term)
        return gallery
class GalleryLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()        
    