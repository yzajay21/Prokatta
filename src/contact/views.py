from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


def contact(request):
	template = "contact.html"

	if request.method == "POST" :
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,'ThanK You',
				"alert alert-success alert-dismissible")
	else:
		form = ContactForm()

	context = {
		'form': form,
	}

	return render(request,template,context)