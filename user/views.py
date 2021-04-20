from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'templates/login_form.html')

def signup(request):
    return render(request, 'templates/signup_form.html')


