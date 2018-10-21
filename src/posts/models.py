from django.db.models.signals import pre_save 
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe 
from markdown_deux import markdown
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from .utils import get_read_time
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
class PostManager(models.Manager):
	def active(self,*args,**Kwargs):
		return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance,filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id,instance.title,extension)
	return "%s/%s" %(instance.id,filename)


class Posts(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
	title 		= models.CharField(max_length=120)
	short_description = models.CharField(max_length=200,null=True,blank=True)
	slug		= models.SlugField(unique=True)
	image 		= models.ImageField(upload_to="upload_location",null=True,blank=True,)#width_field="width_field",height_field="height_field")
	#height_field= models.IntegerField(default=0)
	#width_field= models.IntegerField(default=0)
	posts_image = ImageSpecField(source='image',processors=[ResizeToFill(600,600)],format='JPEG',options={'quality':100})
	image_thumbnail = ImageSpecField(source='image',processors=[ResizeToFill(500,400)],format='JPEG',options={'quality':90})
	draft		= models.BooleanField(default=False)
	publish		= models.DateField(auto_now=False,auto_now_add=False)

	content		= models.TextField()
	read_time  	= models.IntegerField(default=0)#models.TimeField(null=True,blank=True)
	categories  =  models.ManyToManyField('Category', blank=True)
	#content		= RichTextField()
	tags 		= TaggableManager()
	updated		= models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp	= models.DateTimeField(auto_now=False,auto_now_add=True)
	objects 	= PostManager()


	class Meta:
		verbose_name_plural = "Posts"
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blogs:detail", kwargs={"slug": self.slug})



	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)

	
def create_slug(instance,new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Posts.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
	if instance.content:
		html_string = instance.get_markdown()
		read_time_var   = get_read_time(html_string)
		instance.read_time = read_time_var
pre_save.connect(pre_save_post_receiver,sender=Posts)


class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	image 		= models.ImageField(upload_to="upload_location",null=True,blank=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("category:category_detail", kwargs={"slug": self.slug })



class Comments(models.Model):
	post 	= models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
	name  	= models.CharField(max_length=20)
	email 	= models.EmailField()
	body  	= models.TextField()
	created = models.DateTimeField(auto_now_add=True,)
	updated = models.DateTimeField(auto_now=True)
	parent  = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
	active 	= models.BooleanField(default=True)


	class Meta:
		ordering = ('created',)


	def __str__(self):
		return 'Comment by {} on {} '.format(self.name,self.post)

	def children(self):
		return Comments.objects.filter(parent=self)

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True
