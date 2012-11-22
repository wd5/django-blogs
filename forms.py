from django import forms

from . models import BlogsBlog, BlogsPost, BlogsPostImage

class BlogsBlogEditForm( forms.ModelForm ):

    class Meta:
        model = BlogsBlog
        exclude = ( 'author', 'status', )
