from django.contrib import admin
from .models import Author,Book,Category,Wishlist,Buy
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Wishlist)
admin.site.register(Buy)

