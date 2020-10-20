from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse

from .forms import UserRegisterForm, UserLoginForm

# Create your views here.

'''
用户的登录状态是保存在request.user中。如果没有登录，则request.user为AnonymousUser对象。
如果用户登录后，则request.user为User对象。
'''


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def register(request):
    """
       定义注册方法
    """

    if request.method == 'POST':
        # 校验页面中传递的参数，是否填写完整
        form = UserRegisterForm(request.POST)
        # is_valid():判断表单是否验证通过
        if not form.is_valid():
            print('注册校验失败')
        if form.is_valid():
            # 获取校验后的用户名和密码
            print('注册校验成功')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # 创建普通用户create_user，创建超级管理员用户create_superuser
            User.objects.create_user(username=username, password=password)
            # 实现跳转
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        # 表单验证，用户名和密码是否填写，校验用户名是否注册
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print('登录校验成功')
            # 校验用户名和密码，判断返回的对象是否为空，如果不为空，则为user对象
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user:
                # 用户名和密码是正确的,则登录
                auth.login(request, user)
                print('登录成功')
                return HttpResponseRedirect(reverse('main:index'))
            else:
                # 密码不正确
                print('密码错误，请重新登录')
                return render(request, 'login.html', {'error': '密码错误'})
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    if request.method == 'GET':
        # 注销
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))
