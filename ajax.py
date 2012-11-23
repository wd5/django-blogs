from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from zokiguide.decorators import render_to_json

from . models import BlogsPost, BlogsPostImage
from . forms import BlogsImageUploadForm

@login_required
@render_to_json
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
@render_to_json
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
