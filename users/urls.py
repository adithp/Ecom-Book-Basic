from django.urls import path
from .views import register,book_create,author_create,listshow,viewlogin,viewlogout,listeach,add_category,book_update,wishlist_show,add_wish,remove_wish,add_buys,remove_buys,admin_panel,borrow_books

from django.conf.urls import handler404


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
    path('add_category/',add_category,name='add_category'),
    path('wishlist_show/',wishlist_show,name='wishlist_show'),
    path('add_wish/<int:id>/',add_wish,name='add_wish'),
    path('removewish_list/<int:id>/',remove_wish,name='remove_wish_list'),
    path('add_buy/<int:id>/',add_buys,name='add_buys'),
    path('remove_buy/<int:id>/',remove_buys,name='remove_buy'),
    path('admin_panel/',admin_panel,name='admin_panel'),
    path('borrow_books/',borrow_books,name='borrow_books')
]

handler404 = 'users.views.handle404'