from django.contrib import admin

from common.admin import CommonPostAdmin
from . models import BlogsBlog, BlogsPost, BlogsPostImage 

class BlogsBlogAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status' )

class BlogsPostAdmin( admin.ModelAdmin ):
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status' )
    search_fields = ( 'title', 'author', )
    list_filter = ( 'date_edit', )

    
admin.site.register( BlogsBlog, BlogsBlogAdmin )
admin.site.register( BlogsPost, BlogsPostAdmin )
