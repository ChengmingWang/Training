
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User


class UserForm(forms.Form):
    username = forms.CharField(label='user name',max_length=50,help_text='max length 50')
    password = forms.CharField(label='password',widget=forms.PasswordInput(),help_text='max length 50')

def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username= username,password=password)
            return HttpResponse('register successfully!!')
    else:
        uf = UserForm()
        context = {'uf':uf}
        return render(request, 'regist.html', context)

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    context = {'uf': uf}
    return render(request, 'login.html', context)

def index(request):
    username = request.COOKIES.get('username','no user')
    return render_to_response('index.html' ,{'username':username})

def logout(request):
    response =HttpResponseRedirect("/login/",content='log out !!')
    response.delete_cookie('username')
    return response