# -*- coding: utf-8 -*- 

from django.http import HttpResponseRedirect as redirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_auth
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
	if request.POST['user'] and request.POST['pass']:
		u = request.POST['user']
		p = request.POST['pass']

		user = authenticate(username=u, password=p)
		data = {}

		if user is not None:
			login_auth(request, user)
			data["user"] = user.username
		else:
			data["errors"] = "No existe un usuario con ese nombre."
	
	return HttpResponse(simplejson.dumps(data))

def logout(request):
	
	auth_logout(request)
	return redirect(reverse("home"))



@csrf_exempt
def singup(request):
	if request.user.is_authenticated():
		return redirect(reverse("home"))

	data = {}
	username = request.POST["user"]
	password = request.POST["pass"]
	email = request.POST["email"]

	user = User.objects.filter(username=username)
	
	if not user:
		# user was created
		# set the password here
		u = User.objects.create(username=username, password=password, email=email)
		u.save()
		
		u.backend = "django.contrib.auth.backends.ModelBackend"
		login_auth(request, u)
		data["user"] = u.username
	else:
		# user was retrieved
		data["duplicated_user"] = True


	return HttpResponse(simplejson.dumps(data))

@login_required
def index(request):
	return render(request, "index_users.html")