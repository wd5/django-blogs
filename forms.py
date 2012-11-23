from django import forms

from . models import BlogsBlog, BlogsPost, BlogsPostImage

class BlogsBlogEditForm( forms.ModelForm ):

    class Meta:
        model = BlogsBlog
        exclude = ( 'author', 'status', )


class BlogsPostEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super( BlogsPostEditForm, self ).__init__( *args, **kwargs )
        try:
            author = self.instance.author.id
            self.fields['blog'].queryset = BlogsBlog.objects.filter( author = author )
        except:
            pass

    class Meta:
        model = BlogsPost
        exclude = ( 'author', 'status', 'image', )
        fields = ( 'blog', 'title', 'content', 'tags' )

class BlogsImageUploadForm( forms.ModelForm ):
    post = forms.ModelChoiceField( 
        queryset = BlogsPost.objects.all(),
        widget = forms.HiddenInput()
    )

    class Meta:
        model = BlogsPostImage
