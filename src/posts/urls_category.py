from django.urls import path
from posts.views import (
						CategoryListView,CategoryDetailView,	
						
						
					)

app_name = 'posts'

urlpatterns = [

	path('',CategoryListView.as_view(), name='category'),
	path('<slug:slug>/',CategoryDetailView.as_view(), name='category_detail'),
]