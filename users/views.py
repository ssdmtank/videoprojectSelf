
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from django.views import generic
from ratelimit.decorators import ratelimit
from .form import ProfileForm, SignUpForm, UserLoginForm, PasswordChangeForm

# Create your views here.

User = get_user_model()

# 登录
def login(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.clean().data.get('password')
            user = authenticate(username=username, password=password)
            
