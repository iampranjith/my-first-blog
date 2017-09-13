from django import forms    #django forms
from .models import Post    #Post clas from model

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
