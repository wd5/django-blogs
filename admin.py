from django.contrib import admin

from common.admin import CommonPostAdmin
from . models import BlogsBlog, BlogsPost, BlogsPostImage 

class BlogsBlogAdmin(admin.ModelAdmin):
    pass

class BlogsPostAdmin( admin.ModelAdmin ):
    search_fields = ( 'title', )
    list_filter = ( 'date_edit', )
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status' )
    
admin.site.register( BlogsBlog, BlogsBlogAdmin )
admin.site.register( BlogsPost, BlogsPostAdmin )
