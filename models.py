from django.db import models
from django.contrib.auth.models import User
#from django.utils.html import strip_tags
from django.conf import settings
#
#from mptt.models import MPTTModel, TreeForeignKey
#from tinymce import models as tinymce_models
from slugify import slugify
#from tagging.fields import TagField
#from tagging.models import Tag

from common.models import CommonCategory, CommonPost, CommonPostImage

# Create your models here.

def image_upload_to( instance, filename ):
    ext = filename.split( '.' )[-1]
    filename = "%s.%s" % ( uuid.uuid4(), ext.lower() )
    id = str( instance.post.id )
    return 'blogs/%s/%s/%s' % ( id[:1], id, filename )

class BlogsBlog( models.Model ):
    author = models.ForeignKey( User )
    title = models.CharField( max_length = 200, blank = True )
    description = models.TextField( blank = True )
    status = models.CharField( 
        max_length = 15,
        choices = settings.STATUS_CHOICES,
        default = 'active',
        db_index = True
    )
    date_add = models.DateTimeField( auto_now_add = True, null=True )
    date_edit = models.DateTimeField( auto_now = True,null=True )


    def __unicode__( self ):
        return self.title

    def slug( self ):
        return slugify( self.title )


class BlogsPost( CommonPost ):
    blog = models.ForeignKey( BlogsBlog, blank = True )
    image = models.ForeignKey( 'BlogsPostImage', blank = True, null = True )


class BlogsPostImage( CommonPostImage ):
    post = models.ForeignKey( BlogsPost )
    image = models.ImageField( upload_to = image_upload_to )
