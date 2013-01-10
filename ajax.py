from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

from common.decorators import json_response
from common.utils import log

from . models import BlogsPost, BlogsPostImage, BlogsPostComment
from . forms import BlogsImageUploadForm, BlogsPostCommentForm

@login_required
@json_response
def image_upload( request ):

    id = int( request.POST['post'] )

    try:
        post = BlogsPost.objects.get( pk = id )
    except BlogsPost.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = BlogsImageUploadForm( request.POST, request.FILES )
        if form.is_valid():
            image = form.save()

    data = {
        'post':{
            'id':post.id,
        },
        'image':{
            'id':image.id,
            'x100':image.x100.url,
            'x150':image.x150.url,
            'x138':image.x138.url,
            'x450':image.x450.url,
        },
    }

    return data

@login_required
@json_response
def primary( request ):

    post_id = int( request.POST['post_id'] )
    image_id = int( request.POST['image_id'] )

    try:
        post = BlogsPost.objects.get( pk = post_id )
    except BlogsPost.DoesNotExist:
        raise Http404

    try:
        image = BlogsPostImage.objects.get( pk = image_id )
    except BlogsPostImage.DoesNotExist:
        raise Http404

    post.image = image
    post.save()

    data = {
        'result':'ok',
    }

    return data

@login_required
@json_response
def save_comment( request ):

    post_id = int( request.POST['post'] )
    log(str(post_id))
    log(str(request.POST['parent']))
    try:
        post = BlogsPost.objects.get( pk = post_id )
    except BlogsPost.DoesNotExist:
        raise Http404

#    log(post)
    comment = ''

    if request.method == "POST":
        form = BlogsPostCommentForm( request.POST )
        log(str(form))
        if form.is_valid():
            comment = form.save()
            log(comment)


    data = {
        'status':'success',
        'message':'',
        'result':comment,
    }

    return data
