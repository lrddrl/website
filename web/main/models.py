from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Expert(models.Model):
    E_fname    = models.CharField(max_length=100)
    E_lname    = models.CharField(max_length=100)
    # E_username = models.CharField(max_length=100)
    # E_email    = models.CharField(max_length=100)
    # E_password = models.CharField(max_length=100)
    E_phone    = models.CharField(max_length=100,null=True)
    # date_created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '%s-%d-%d'%(self.E_fname, self.E_password, self.date_created)

class Customer(models.Model):
    C_fname    = models.CharField(max_length=100)
    C_lname    = models.CharField(max_length=100)
    C_username = models.CharField(max_length=100)
    C_email    = models.CharField(max_length=100)
    C_password = models.CharField(max_length=100)
    C_phone    = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%d-%d'%(self.C_fname, self.C_password, self.date_created)


class Customer_picuture(models.Model):
    user = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='photos/')


class mypicture(models.Model):    
    user = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='photos/')
    #关联外键 
    #Ename   = models.ForeignKey(
    #     'name',
    #    on_delete = models.CASCADE,
    #)