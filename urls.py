from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'blogs',
    url( r'^add-blog/$', 'views.add_blog', name = 'add-blog' ),
    url( r'^edit-blog/(?P<id>\d+)$', 'views.edit_blog', name = 'edit-blog' ),
    url( r'^add-post/$', 'views.add_post', name = 'add-post' ),
    url( r'^edit-post/(?P<id>\d+)/$', 'views.edit_post', name = 'edit-post' ),
    url( r'^blog-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?/(?:/?page-(?P<page>\d+)/)?$', 'views.blog', name = 'blog' ),
    url( r'^post-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?/$', 'views.post', name = 'post' ),
    url( r'^ajax/image-upload/$', 'ajax.image_upload', name = 'ajax-image-upload' ),
    url( r'^ajax/primary/$', 'ajax.primary', name = 'ajax-primary' ),
    url( r'ajax/save-comment', 'ajax.save_comment', name='save-comment' ),
    url( r'^$', 'views.home', name = 'home' ),
 )

