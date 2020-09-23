from django import forms
from django.views.generic import CreateView

from .models import Post

class PostCreate(CreateView):
    class Meta:
        model=Post
