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


def custom_login(request):
	if request.user.is_authenticated():
		return redirect(reverse("index"))
	else:
		return login(request)

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


def register(request):
	if request.user.is_authenticated():
		return redirect(reverse("index"))

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return redirect(reverse("login"))
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {
		'form': form,
	})

@login_required
def index(request):
	return render(request, "index_users.html")