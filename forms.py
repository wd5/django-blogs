from django import forms
from django.contrib.auth.models import User

from common.forms import CommonPostCommentForm
from . models import BlogsBlog, BlogsPost, BlogsPostImage, BlogsPostComment

class BlogsBlogEditForm( forms.ModelForm ):

    class Meta:
        model = BlogsBlog
        exclude = ( 'author', 'status', )


class BlogsPostEditForm( forms.ModelForm ):
    def __init__( self, *args, **kwargs ):
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

class BlogsPostCommentForm( CommonPostCommentForm ):
#    parent = forms.ModelChoiceField(
#        queryset = BlogsPostComment.objects.all(),
#        widget = forms.HiddenInput(),
#    )
    post = forms.ModelChoiceField( 
        queryset = BlogsPost.objects.all(),
        widget = forms.HiddenInput(),
    )
    author = forms.ModelChoiceField( 
        queryset = User.objects.all(),
        widget = forms.HiddenInput(),
    )

    class Meta( CommonPostCommentForm.Meta ):
        model = BlogsPostComment
