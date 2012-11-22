from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'blogs',
    url( r'^add-blog/$', 'views.add_blog', name = 'blogs-add-blog' ),
    url( r'^edit-blog/(?P<id>\d+)$', 'views.edit_blog', name = 'blogs-edit-blog' ),
    url( r'^add-post/$', 'views.add_post', name = 'blogs-add-post' ),
    url( r'^edit-post/(?P<id>\d+)$', 'views.edit_post', name = 'blogs-edit-post' ),
    url( r'^blog-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?/(?:/?page-(?P<page>\d+)/)?$', 'views.blog', name = 'blogs-blog' ),
    url( r'^post-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?/$', 'views.post', name = 'blogs-post' ),
    url( r'^$', 'views.home', name = 'blogs-home' ),
#    url( r'^edit/(?P<id>\d+)$', 'views.edit', name = 'catalog-edit' ),
#    url( r'^category-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?(?:\/loc\-(?P<country>\d+))?(?:\:(?P<city>\d+))?(?:\/page-(?P<page>\d+))?', 'views.category', name = 'catalog-category' ),
#    url( r'^post-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?', 'views.post', name = 'catalog-post' ),
#    url( r'^file/$', 'views.file', name = 'catalog-file' ),
#    url( r'^ajax/image-upload/$', 'ajax.image_upload', name = 'catalog-ajax-image-upload' ),
#    url( r'^ajax/primary/$', 'ajax.primary', name = 'catalog-ajax-primary' ),
#    url( r'^(?:loc\-(?P<country>all|\d+))?(?:\:(?P<city>\d+))?(?:/?page-(?P<page>\d+))?', 'views.home', name = 'catalog-home' ),
 )

