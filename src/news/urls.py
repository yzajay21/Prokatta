from django.urls import path
from news.views import newsletter_signup,newsletter_unsubscribe

app_name = 'news'
urlpatterns = [
	path('sign_up/',newsletter_signup,name='newsletter_signup'),
	path('unsubscribe/',newsletter_unsubscribe,name='newsletter_unsubscribe'),
]
