from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^home$',views.home_page, name='home_page'),
	url(r'^login$',views.auth_login, name='auth_login'),
	url(r'^logout$',views.auth_logout, name='auth_logout'),
]
