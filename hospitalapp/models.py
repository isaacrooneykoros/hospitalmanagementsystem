from django.db import models


# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    yearofbirth = models.DateField(null=True)

    def __str__(self):
        return self.full_name


class product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)