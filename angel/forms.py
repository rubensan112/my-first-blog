from django import forms

from .models import Post, Pepito


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
class PostForm1(forms.ModelForm):
    class Meta:
        model = Pepito
        fields = ('title', 'text','fecha','extra',)