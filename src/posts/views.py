from urllib.parse import quote_plus
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import PostForm,CommentsForm
from .models import Posts,Comments,Category
from django.utils import timezone
from .utils import get_read_time

def home(request):
	posts = Posts.objects.active().order_by("-timestamp")[:5]
	images = Posts.objects.filter(images=images).order_by("-timestamp")[:5]
	recents= Posts.objects.active().order_by("-timestamp")[:7]
	featured = Posts.objects.active().order_by("?")[:7]
	category = Category.objects.all().order_by("?")[:3]
	if request.user.is_staff or request.user.is_superuser:
		posts = Posts.objects.all()
	query = request.GET.get("q")
	if query :
		posts = posts.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
			).distinct()
	context = {
		'posts': posts,
		'featured':featured,
		'category':category,
		'recents':recents,
		"images":images,
	}
	return render(request,'index1.html',context)


def posts_home(request):
	posts = Posts.objects.active()
	today = timezone.now().date
	#tag   = None
	if request.user.is_staff or request.user.is_superuser :
		posts = Posts.objects.all()

	
	context = {
		'posts': posts,
		"today" : today,

	}
	return render(request,'posts/post_list.html',context)

def posts_create(request):
	if not request.user.is_staff or not request.user.is_superuser :
		raise Http404

	if not request.user.is_authenticated :
		raise Http404
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request,"Sucessfully created")
		return redirect("blogs:detail")
	else:
		messages.error(request,"Not Sucessfully created")

	context = {
		'form' : form,
	}
	return render(request,'posts/posts_form.html',context)

def posts_detail(request,slug=None):
	posts = Posts.objects.all().order_by("?")[:5]
	related = Posts.objects.all().order_by("?")[:3]
	instance = get_object_or_404(Posts,slug=slug)
	comments = instance.comments.filter(active=True)

	#print(get_read_time(instance.content))
	#print(get_read_time(instance.get_markdown()))
	#if instance.publish > timezone.now().date() or instance.draft:
		#if not request.user.is_staff or not request.user.is_superuser :
			#raise Http404

	share_string  = quote_plus(instance.content)
	new_comment = None
	if request.method =='POST':
		comment_form = CommentsForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post= instance
			new_comment.save()
		return redirect("blogs:detail",slug=obj.slug)

	else:	
		comment_form = CommentsForm()	


	context = {
		'title' : "instance.title",
		'instance': instance,
		"share_string": share_string,
		'comment_form': comment_form,
		'comments' : comments,
		"posts"   :posts,
		"related" :related,
	}	
	return render(request,'posts/detail1.html',context)



def posts_update(request,slug=None):
	if not request.user.is_staff or not request.user.is_superuser :
		raise Http404
	instance = get_object_or_404(Posts,slug=slug)
	form = PostForm(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Sucessfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Not Sucessfully updated")
	context = {
		'title' : "instance.title",
		'instance': instance,
		'form':form,
	}	
	return render(request,'posts/posts_form.html',context)

def posts_delete(request,slug=None):
	if request.user.is_staff or not request.user.is_superuser :
		raise Http404
	instance = get_object_or_404(Posts,slug=slug)
	instance.delete()
	messages.success(request,"Sucessfully deleted")
	return redirect("posts:posts")

class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()
	template_name = "posts/category_list1.html"




class CategoryDetailView(DetailView):
	model = Category

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()

		posts_set = obj.posts_set.all()
		#default_posts = obj.default_category.all()
		posts = posts_set 
		categories = Category.objects.all()
		context["posts"] = posts
		context ["categories"] = categories
		return context

