from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from . models import BlogsBlog, BlogsPost, BlogsPostImage, BlogsPostComment
from . forms import BlogsBlogEditForm, BlogsPostEditForm, BlogsImageUploadForm, BlogsPostCommentForm
from common.utils import log

def get_posts( blog = None, page = None ):

    posts = BlogsPost.objects.filter( status = 'active' )

    if blog:
        posts = posts.filter( blog = blog )

    paginator = Paginator( posts, 7 )

    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page( paginator.num_pages )

    return posts

def home( request ):

    posts = get_posts()

    data = {
        'posts':posts,
    }

    return render( request, 'blogs/home.html', data )

@login_required
def add_blog( request ):
    if request.session.get( 'blogs-blog-draft-id', '' ) and int( request.session['blogs-blog-draft-id'] ) > 0:
        return redirect( 'blogs-edit-blog', id = request.session['blogs-blog-draft-id'] )
    else:
        blog = BlogsBlog( 
            author = User.objects.get( 
                pk = request.user.id
            )
        )
        blog.save()
        request.session['blogs-blog-draft-id'] = blog.id
        return redirect( 'blogs-edit-blog', id = blog.id )

@login_required
def edit_blog( request, id ):
    id = int( id )

    try:
        blog = BlogsBlog.objects.get( pk = id )
    except BlogsBlog.DoesNotExist:
        raise Http404

    form = BlogsBlogEditForm( instance = blog )
    if request.method == "POST":
        form = BlogsBlogEditForm( request.POST, instance = blog )

        if form.is_valid():
            form.save()
            blog.status = 'active'
            blog.save()

            try:
                del request.session['blogs-blog-draft-id']
            except:
                pass

            return redirect( 'blogs-blog', id = id )

    data = {
        'form':form
    }
    return render( request, 'blogs/edit-blog.html', data )

@login_required
def add_post( request ):

    if request.session.get( 'blogs-post-draft-id', '' ) and int( request.session['blogs-post-draft-id'] ) > 0:
        return redirect( 'blogs-edit-post', id = request.session['blogs-post-draft-id'] )
    else:
        post = BlogsPost( status = 'draft', author = User.objects.get( pk = request.user.id ) )
        post.save()
        request.session['blogs-post-draft-id'] = post.id
        return redirect( 'blogs-edit-post', id = post.id )

@login_required
def edit_post( request, id ):

    id = int( id )

    try:
        post = BlogsPost.objects.get( pk = id )
    except BlogsPost.DoesNotExist:
        raise Http404

    user = User.objects.get( pk = request.user.id )

    form = BlogsPostEditForm( instance = post )

    if request.method == "POST":
        form = BlogsPostEditForm( request.POST, instance = post )
        if form.is_valid():
            form.save()
            post.status = 'active'
            post.save()
            try:
                del request.session['blogs-post-draft-id']
            except:
                pass

            return redirect( 'blogs-post', id = id )

    data = {
        'post':post,
        'image_upload_form':BlogsImageUploadForm( initial = {'post':post} ),
        'form':form,
    }
    return render( request, 'blogs/edit-post.html', data )

def blog( request, id, slug = None, page = None ):

    id = int( id )

    try:
        blog = BlogsBlog.objects.get( pk = id )
    except BlogsBlog.DoesNotExist:
        raise Http404

    if blog.slug() != slug:
        return redirect( 'blogs-blog', id = blog.id, slug = blog.slug() )

    posts = get_posts( blog, page )

    data = {
        'blog':blog,
        'posts':posts,
    }
    return render( request, 'blogs/blog.html', data )

def post( request, id, slug = None ):

    id = int( id )

    try:
        post = BlogsPost.objects.get( pk = id )
    except BlogsPost.DoesNotExist:
        raise Http404

    if post.slug() != slug:
        return redirect( 'blogs-post', id = post.id, slug = post.slug() )

    data = {
        'post':post,
    }

    return render( request, 'blogs/post.html', data )
