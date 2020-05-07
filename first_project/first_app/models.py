from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    ## Just a note here, it is generally not a good idea to directly inherit from the user clas, so instead that is why we use the one to one relationship function
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
        # pip install pillow for Image Field use
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        #Built in attribute of django.contrib.auth.models.User
        return self.user.username

class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)


    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return  str(self.date)

class User(models.Model):
    email_address = models.EmailField(max_length= 264, unique = True)
    first_name = models.CharField(max_length= 128)
    last_name = models.CharField(max_length= 128)

    def __str__(self):
        return self.email_address
