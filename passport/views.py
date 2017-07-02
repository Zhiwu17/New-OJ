from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import HttpResponse
from django.template import RequestContext, Context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, render_to_response
from passport.models import UserProfile

def userDemo(request):
    desc = UserProfile.objects.all()[0].description
    return HttpResponse(desc)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('Account', '')
        password = request.POST.get('Password', '')
        user = authenticate(username = username, password = password)
        if user and user.is_active:
            login(request, user)
            return render_to_response('index.html', locals(), RequestContext(request))
        else:
            return HttpResponse('Login UNSUCCESS')
    return render_to_response('login.html', locals(), RequestContext(request))

def userLogout(request):
    logout(request)
    return render_to_response('index.html', locals(), RequestContext(request))

def userInfor(request, name=''):
    user = User.objects.get(username=name)
    username = user
    return render_to_response('user.html', locals(), RequestContext(request))
