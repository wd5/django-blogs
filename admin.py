from django.contrib import admin

from common.admin import CommonPostAdmin
from . models import BlogsBlog, BlogsPost, BlogsPostImage, BlogsPostComment

class BlogsBlogAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status' )

class BlogsPostAdmin( admin.ModelAdmin ):
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status' )
    search_fields = ( 'title', 'author', )
    list_filter = ( 'date_edit', )

class BlogsPostCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register( BlogsBlog, BlogsBlogAdmin )
admin.site.register( BlogsPost, BlogsPostAdmin )
admin.site.register(BlogsPostComment, BlogsPostCommentAdmin)
