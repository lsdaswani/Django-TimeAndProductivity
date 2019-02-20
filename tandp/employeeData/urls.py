from django.conf.urls import url
from .import views

urlpatterns = [ 
	url(r'^$',views.process_data, name = 'process_data'),
	

]