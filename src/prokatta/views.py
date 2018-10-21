from urllib.parse import quote_plus
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#from .forms import PostForm,CommentsForm
from posts.models import Posts,Comments,Category
from django.utils import timezone
from posts.utils import get_read_time



def home(request):
	posts = Posts.objects.active().order_by("-timestamp")[:5]
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
	}
	return render(request,'index1.html',context)


def about(request):
	return render(request,"about.html",{})

def contact(request):
	return render(request,"contact.html",{})