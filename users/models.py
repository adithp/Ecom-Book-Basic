from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

    
    
class Book(models.Model):
    title = models.CharField(max_length=30,null=False)
    isbn = models.CharField(max_length=18,null=False)
    description = models.TextField(null=False)
    writed = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='',null=True)
    available = models.BooleanField(default=True,null=False)
    
    
    
    
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'book')


class Buy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    
    