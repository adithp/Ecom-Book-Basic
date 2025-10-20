from django.urls import path
from .views import register,book_create,author_create,listshow,viewlogin,viewlogout,listeach,add_category,book_update


urlpatterns = [
    path('register/',register,name='register'),
    path('login/',viewlogin,name="viewlogin"),
    path('logout',viewlogout,name='logout'),
    path('book_create/',book_create,name='book_create'),
    path('author_create/',author_create,name='author_create'),
    path('show/',listshow,name='show'),
    path('',listshow,name='show'),
    path('show/<int:id>/',listeach,name='listeach'),
    path('update/<int:id>/',book_update,name='book_update'),
    path('add_category/',add_category,name='add_category')
]