from urllib import request

from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib import messages

from .models import Post,Product
from .forms import PostCreate
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return render(request,'Rakesh/Index.html',{})

# Contact
def contact(request):
    tabl=Post.objects.all()

    return render(request,'Rakesh/contact.html',{'t':tabl,})

def about(request):
    return render(request,'Rakesh/about.html',{})

class createvieww(CreateView):
    model = Post
    template_name = 'Rakesh/createfrom.html'
    fields = '__all__'



def product(request):
    tb=Product.objects.all()
    return render(request,'Rakesh/product.html',{'tb':tb})



