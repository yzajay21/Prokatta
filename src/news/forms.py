from django import forms
from crispy_forms.helper import FormHelper

from .models import Newsletters

class NewsletterUserSignUpForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_show_lables = False
	class Meta :
		model = Newsletters
		fields = ['email']

		def clean_email(self):
			email = self.cleaned_data.get()

			return email