from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Author,Book,Category
from .forms import BookForm,AuthorForm,CategoryForm
from django.http import HttpResponse
# Create your views here.


def listshow(req):
    
    category = Category.objects.all()
    dataset = {}
    for i in category:
        dataset[i] = Book.objects.filter(category=i.id)
        
    return render(req,'show.html',{'data':dataset})


def listeach(req,id):
    
    if Book.objects.filter(id=id).exists():
        item = Book.objects.get(id=id)
        print(item.title)
        return render(req,'showeach.html',{'data':{'item':item}})
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
            form = BookForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('show')
        return render(req,'book_form.html',{'form':form})
    else:
        return HttpResponse('Only Admin Can Access')
    
@login_required
def book_update(req,id):
    if req.user.is_superuser:
        if Book.objects.filter(id=id).exists():
            
            book = Book.objects.get(id=id)
            
            if req.method == 'POST':
                
                form = BookForm(req.POST,instance=book)
                if form.is_valid():
                    form.save()
                    redirect('listeach',id=id)
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