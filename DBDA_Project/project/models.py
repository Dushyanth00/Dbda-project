from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Files(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

#class Venue(models.Model):
 #   name = models.CharField('Venue Name', max_length=120)
  #  address = models.CharField(max_length=300)
   # zip_code = models.CharField('Zip Code', max_length=15)
    #phone = models.CharField('Contact Phone', max_length=25, blank=True)
    #web = models.URLField('Website Address', blank=True)
    #email_address = models.EmailField('Email Address', blank=True)
    #owner = models.IntegerField("Venue Owner", blank=False, default=1)
    #venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

    #def __str__(self):
        #return self.name