#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/23

from django.shortcuts import render
from django.utils.safestring import mark_safe
from arya.service import v1
from . import models


class HostInfoConfig(v1.AryaConfig):
    """
    自定义主机信息展示UI
    """

    def del_func(self, row):
        """
        删除标签
        :param row:
        :return:
        """
        app_name = self.model_class._meta.app_label
        model_name = self.model_class._meta.model_name
        row_id = row.id
        return mark_safe("<a href='/{0}/{1}/{2}/delete/'>删除</a>".format(app_name, model_name, row_id))

    list_display = ['hostname', 'business', 'idc', 'os', 'cpu', 'mem', 'disk', 'status', 'owner', del_func]

    def changelist_view(self, request):
        """
        列表试图
        :param request:
        :return:
        """
        data_list = []
        queryset = self.model_class.objects.all()
        for row in queryset:
            if not self.list_display:
                data_list.append([row, ])
            else:
                temp = []
                for column_or_func in self.list_display:
                    if isinstance(column_or_func, str):
                        temp.append(getattr(row, column_or_func))
                    else:
                        temp.append(column_or_func(self, row))
                data_list.append(temp)
        print(data_list)
        return render(request, 'arya/changelist.html', {'data_list': data_list})


class BusiNessConfig(v1.AryaConfig):
    """
    自定义业务线展示UI
    """
    list_display = ['title']


v1.site.register(models.HostInfo, HostInfoConfig)
v1.site.register(models.BusiNess, BusiNessConfig)
