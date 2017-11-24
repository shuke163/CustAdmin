#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/23
from django.conf.urls import url
from django.shortcuts import render, HttpResponse, redirect


class AryaConfig(object):
    """
    每个models类的URL对应处理的View实现
    """

    def __init__(self, model_class, site):
        self.model_class = model_class
        # View对象
        self.site = site

    @property
    def urls(self):
        partterns = [
            url(r'^$', self.changelist_view),
            url(r'^add/', self.add_view),
            url(r'^(\d+)/change/$', self.change_view),
            url(r'^(\d+)/delete/$', self.delete_view)
        ]
        return partterns

    def changelist_view(self, request):
        """
        列表试图
        :param request:
        :return:
        """
        # return HttpResponse("列表页面")
        return render(request, 'arya/changelist.html')

    def add_view(self, request):
        """
        添加试图
        :param request:
        :return:
        """
        return HttpResponse("添加试图")

    def change_view(self, request):
        """
        修改试图
        :param request:
        :return:
        """
        return HttpResponse("修改试图")

    def delete_view(self, request):
        """
        删除试图
        :param request:
        :return:
        """
        return HttpResponse("删除试图")


class AryaSite(object):
    """
    实现类似于admin.site.register()功能
    """

    # 存放所有的models类及对应处理UTRL的的view对象
    def __init__(self):
        self._registry = {}

    def register(self, class_name, config_class):
        """
        注册方法,封装对象
        self._registry = {
            module.UserInfo: obj1,  # obj1 = AryaConfig(models.UserInfo,site),
            module.UserType: obj2,  # obj2 = AryaConfig(models.UserType,site),
        }
        :param class_name: models类
        :param config_class: 对应的View类(AryaConfig)
        :return:
        """
        self._registry[class_name] = config_class(class_name, self)

    @property
    def urls(self):
        """
        处理子路由
        :return:
        """
        partterns = [
            url(r'^login/$', self.login),
            url(r'^logout/$', self.logout),
        ]
        # 循环self._registry属性里面的每一个元素，key为models类，value为URLS对应处理的类obj对象
        for model_class, arya_config_obj in self._registry.items():
            # 分别为app名称和models的类名称
            # print("*" * 50)
            # print(model_class._meta.app_label, model_class._meta.model_name)
            app_model_name_urls = r'^{0}/{1}/'.format(model_class._meta.app_label, model_class._meta.model_name)
            # arya_config_obj.urls self._registry字典中存放的values对象obj下面的urls方法
            pt = url(app_model_name_urls, (arya_config_obj.urls, None, None))
            partterns.append(pt)
        # 3元组
        return partterns, None, None

    def login(self):
        """
        登陆
        :return:
        """
        return redirect('login')

    def logout(self):
        """
        退出
        :return:
        """
        return redirect('login')


# 实例化，利用单例模式
site = AryaSite()
