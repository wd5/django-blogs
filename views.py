from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from . models import BlogsBlog, BlogsPost, BlogsPostImage
#from . forms import CatalogEditForm, ImageUploadForm
from common.utils import log

def home( request ):
    data = {}
    return render( request, 'blogs/home.html', data )

@login_required
def add_blog( request ):
    if request.session.get( 'blogs-draft-id', '' ) and int( request.session['blogs-draft-id'] ) > 0:
        return redirect( 'blogs-edit', id = request.session['blogs-draft-id'] )
    else:
        post = BlogsBlog( author = User.objects.get( pk = request.user.id ) )
        post.save()
        request.session['blogs-draft-id'] = post.id
        return redirect( 'blogs-edit-blog', id = post.id )

@login_required
def edit_blog( request, id ):
    data = {}
    return render( request, 'blogs/edit-blog.html', data )

@login_required
def add_post( request ):
    data = {}
    return render( request, 'blogs/edit-post.html', data )

@login_required
def edit_post( request, id ):
    data = {}
    return render( request, 'blogs/edit-post.html', data )

def blog( request, id, slug = None ):
    data = {}
    return render( request, 'blogs/edit-post.html', data )

def post( request, id, slug = None ):
    data = {}
    return render( request, 'blogs/edit-post.html', data )
