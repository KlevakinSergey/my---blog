from django import forms
from . models import Post 
from .models import SimpleAddPhoto

class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ('title', 'text',)
     


class SimpleAddPhotoForm(forms.ModelForm):
    class Meta:
        model = SimpleAddPhoto
        fields = ('title', 'description', 'care', 'photo')     