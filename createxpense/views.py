from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import TransactionTypes, TransactItems
from django.contrib.auth import authenticate, login , logout
# Create your views here.


def index(request):
	return render(request,'index.html')


def auth_login(request):
	us = request.POST['usernameid']
	ps = request.POST['passwordid']
	user = authenticate(request,username=us,password=ps)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect('/expense/home')
	else:
		return render(request,'login.html',{'err':'True'});

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/expense')



def home_page(request):
	if request.user.is_authenticated():
		return render(request,'home.html',{'fname':request.user.get_short_name()})
	else:
		return render(request,'login.html')
