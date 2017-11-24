#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/23

from django.shortcuts import render, redirect
from app01 import models


def login(request):
    """
    登陆
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if obj:
            request.session['userinfo'] = {'username': obj.username, 'is_login': True}
            return redirect('index')
        return render(request, 'login.html', {'msg': '用户名或密码错误'})


def logout(request):
    """
    退出
    :param request:
    :return:
    """
    if request.method == "GET":
        return redirect('login')


def index(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'index.html')
