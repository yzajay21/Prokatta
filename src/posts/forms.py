from django import forms
from .models import Posts,Comments
from pagedown.widgets import PagedownWidget
class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model 	= Posts
		fields 	= ['title','short_description','content','image','draft','publish','categories','tags',]




class CommentsForm(forms.ModelForm):
	class Meta:
		model = Comments	
		fields = ('name','email','body')

