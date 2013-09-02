# -*- coding: utf-8 -*- 

from django.http import HttpResponseRedirect as redirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate


def custom_login(request):
	if request.user.is_authenticated():
		return redirect(reverse("index"))
	else:
		return login(request)

def login(request):
	
	user = authenticate(username='john', password='secret')
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
	        print("User is valid, active and authenticated")
	    else:
	        print("The password is valid, but the account has been disabled!")
	else:
	    # the authentication system was unable to verify the username and password
	    print("The username and password were incorrect.")

def logout(request):
	
	auth_logout(request)
	return redirect(reverse("login"))


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