# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

# Create your views here.

def get_base_context():
    context = dict()
    return context

def index(request):
    context = get_base_context()
    return render(request, 'main.html', context)

def register_user(request):
    username = request.GET.get('username', None)
    if username is not None:
        new_user, created = User.objects.get_or_create(username=username)
        if created:
            new_user.first_name = request.GET.get('first_name', '')
            new_user.last_name  = request.GET.get('last_name', '')
            new_user.save()
    return redirect('/')

def login(request):
    username = request.GET.get('username', 'admin')
    user = User.objects.get(username=username)
    django_login(request, user)
    return redirect('/')

def logout(request):
    django_logout(request)
    return redirect('/')

def private_page(request):
    if not request.user.is_authenticated():
        raise PermissionDenied

    context = get_base_context()
    return render(request, 'private.html', context)

