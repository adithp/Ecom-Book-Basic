from django import forms
from django.forms import ValidationError
from .models import Book
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class BookForm(forms.ModelForm):
    
    
    
    class Meta():
        model = Book
        fields = ['title','author','price','writed','description','isbn','category','image',]
        widgets = {
            'writed':forms.DateInput(attrs={'type':'date','class':'parthiv'}),
            'description':forms.Textarea()
        }


class AuthorForm(forms.Form):
    name = forms.CharField(required=True)
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if len(name) < 3:
            raise ValidationError("name must be 3 characters")
        
        return name
    
    
class CategoryForm(forms.Form):
    name = forms.CharField(required=True)
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if len(name) < 3:
            raise ValidationError("name must be 3 characters")
        
        return name

