from django.conf.urls import url
from profiles.views import ProfileView

urlpatterns = [
	url(r'^policy/$',ProfileView.as_view())    
]