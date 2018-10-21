from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
#from .views import contact
from .views import home,about,contact
#from django.contrib.sitemaps.views import sitemap
#from posts.sitemaps import PostSitemap
#sitemaps = {
##'posts': PostSitemap,
#}
urlpatterns = [
	path('posts/',include('posts.urls',namespace='blogs')),
	path('',home,name='home'),
	path('category/',include('posts.urls_category',namespace='category')),
    path('newsletter/',include("news.urls",namespace='newsletter')),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
 #   path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'ProKatta'
admin.site.site_title = 'ProKatta'