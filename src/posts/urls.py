from django.urls import path
from posts.views import (home,
						posts_home,posts_detail,
						posts_create,posts_update,posts_delete,
						CategoryListView,CategoryDetailView,	
						
						
					)

app_name = 'posts'
urlpatterns = [
	#path('',home,name='home'),
	path('blogs/',posts_home,name='posts'),
	path('create/',posts_create,name='create'),
	path('blogs/<slug:slug>/edit/',posts_update,name='update'),
	path('blogs/<slug:slug>/',posts_detail,name='detail'),
	path('blogs/<slug:slug>/delete/',posts_delete,name='delete'),
	
	#path('contact/',contact,name='contact')
   
]

