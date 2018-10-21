from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from .models import Newsletters
from .forms import NewsletterUserSignUpForm


def newsletter_signup(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if Newsletters.objects.filter(email=instance.email).exists():
			messages.warning(request,'Your Email Already exists in our database',"alert alert-warning alert-dismissible")
		else:
			instance.save()
			messages.success(request,'Thank You For Subscribing!',
				"alert alert-success alert-dismissible")
	context = {
		'form': form
	}
	template = "news/sign_up.html"

	return render(request,template,context)


def newsletter_unsubscribe(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)

		if Newsletters.objects.filter(email=instance.email).exists():
			Newsletters.objects.filter(email=instance.email).delete()
			messages.success(request,"Your Email has been removed","alert alert-success alert-dismissible")
		else:
			messages.warning(request,"Your Email not in database","alert alert-warning alert-dismissible")

	context = {
		'form': form
	}
	template = "news/unsubscribe.html"

	return render(request,template,context)