from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Author,Book,Category,Wishlist,Buy
from .forms import BookForm,AuthorForm,CategoryForm
from django.http import HttpResponse
# Create your views here.


def listshow(req):
    
    category = Category.objects.all()
    dataset = {}
    for i in category:
        dataset[i] = Book.objects.filter(category=i)
        
    return render(req,'show.html',{'data':dataset})


def listeach(req,id):
    
    if Book.objects.filter(id=id).exists():
        item = Book.objects.get(id=id)
        user = req.user
        wish = None
        if  Wishlist.objects.filter(user=user,book=item).exists():
            wish = Wishlist.objects.get(user=user,book=item)
            print(wish)
        return render(req,'showeach.html',{'data':{'item':item,'wish':wish}})
    else:
        HttpResponse('Book Not Found')

@login_required
def author_create(req):
    if req.user.is_superuser:
        form = AuthorForm()
        
        if req.method == 'POST':
            form = AuthorForm(req.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                Author.objects.create(name=name)
                return redirect ('register')
        
        
        
        return render(req,'book_form.html',{'form':form})
    else:
        return HttpResponse('Access only for admin')

@login_required
def add_category(req):
    if req.user.is_superuser:
        form = CategoryForm()
        
        if req.method == 'POST':
            form = CategoryForm(req.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                Category.objects.create(name=name)
                return redirect('show')
        
        
        
        return render(req,'book_form.html',{'form':form})
    else:
        return HttpResponse('Access only for admin')

@login_required
def book_create(req):
    if req.user.is_superuser:
        
        form = BookForm()
        if req.method == 'POST':
            form = BookForm(req.POST,req.FILES)
            if form.is_valid():
                form.save()
                return redirect('show')
        return render(req,'book_form.html',{'form':form})
    else:
        return HttpResponse('Only Admin Can Access')
    
    
@login_required
def admin_panel(req):
    if req.user.is_superuser: 
        return render(req,'admin.html')

    
@login_required
def book_update(req,id):
    if req.user.is_superuser:
        if Book.objects.filter(id=id).exists():
            
            book = Book.objects.get(id=id)
            
            if req.method == 'POST':
                
                form = BookForm(req.POST,instance=book)
                if form.is_valid():
                    form.save()
                    return redirect('listeach',id=id)
            form = BookForm(instance=book)
            return render(req,'book_form.html',{'form':form})
        else:
            return HttpResponse('Book Not Found')
    else:
        return HttpResponse('Only Admin Can Access')


def register(req):
    if req.user.is_authenticated:
        return redirect('show')
    form = UserCreationForm()
    
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        
        if form.is_valid():
            form.save()
            return redirect('show')
    
    
    
    
    return render(req,'login.html',{'form':form})


    
def viewlogout(req):
    logout(req)
    return redirect('show')
    
    
def viewlogin(req):
    if req.user.is_authenticated:
        return redirect('show')
    form = AuthenticationForm()
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        
        user = authenticate(req,username=username,password=password)
        
        if user is not None:
            login(req,user)
            return redirect('show')
        
            
    
    return render(req,'login.html',{'form':form})  


@login_required
def add_wish(req,id):
    
        if Book.objects.filter(id=id).exists():
        
            user = req.user
            book = Book.objects.get(id=id)
            if Wishlist.objects.filter(user=user,book=book).exists():
                return HttpResponse('It already in the wishlist')
            
            obj = Wishlist.objects.create(
                user=user,
                book=book   
            )
            return redirect('listeach',id=id)
            
            
            
        else:
            return HttpResponse('Book Not found')
        
@login_required
def wishlist_show(req):
    if req.user.is_authenticated:
        user = req.user
        lists = Wishlist.objects.filter(user=user)
        print(lists)
        return render(req,'wishlist.html',{'data':lists})
        

@login_required
def remove_wish(req,id):
    
    if Wishlist.objects.filter(id=id).exists():
        source = req.GET.get('from')
        wish = Wishlist.objects.get(id=id)
        
        wish.delete()
        if source == "wishlist":
            return redirect('wishlist_show')
        elif source == 'showeach':
            bokid = req.GET.get('bookid')
            return redirect('listeach',id=bokid)
        # return redirect('show')
        
        
        
    else:
        return HttpResponse('Book Not found')
    
    
@login_required
def add_buys(req,id):
    user = req.user
    if Book.objects.filter(id=id).exists():
        book = Book.objects.get(id=id)
        if Buy.objects.filter(book=book).exists():
            return HttpResponse('Already Taked')
        
        Buy.objects.create(
            book=book,
            user=user
        )
        book.available = False
        book.save()
        return redirect('listeach',id=id)
    return HttpResponse('Book not found')



@login_required
def remove_buys(req,id):
    user = req.user
    if Book.objects.filter(id=id).exists():
        book = Book.objects.get(id=id)
        if Buy.objects.filter(book=book,user=user).exists():
            buy = Buy.objects.get(book=book,user=user)
            buy.delete()
            book.available = True
            book.save()
            return redirect('listeach',id=id)
        else:
            return HttpResponse("Eroor Found book or user not found")
    return HttpResponse('Book not found')

@login_required

def borrow_books(req):
    user = req.user
    
    borrows = Buy.objects.filter(user=user)
    
    return render(req,'mybooks.html',{'borrows':borrows})


    
    
    
    
    
    
    
def handle404(req):
    return render(req,'404.html')
    
