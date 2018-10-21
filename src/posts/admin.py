from django.contrib import admin
from django.db import models
from .models import Posts,Comments,Category
# Register your models here.
from pagedown.widgets import AdminPagedownWidget

class PostAdmin(admin.ModelAdmin):
	list_display       		= ['title','timestamp','updated','user',]
	prepopulated_fields		= {'slug':('title',),}
	list_display_links 		= ['updated',]
	list_editable	   		= ['title']
	
	list_filter        		= ['title','timestamp','updated',]
	search_fields	   		= ['title','content',]
	formfield_overrides = {
		models.TextField:{'widget':AdminPagedownWidget},
	}
	class Meta:
		model = Posts
admin.site.register(Posts,PostAdmin)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}
	
admin.site.register(Category,CategoryAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','created','updated',)
	list_filter	 = ('active','created','updated',)
	search_fields = ('name','email','body',)



admin.site.register(Comments,CommentAdmin)