#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/23

from arya.service import v1
from . import models


class HostInfoConfig(v1.AryaConfig):
    """
    自定义主机信息展示UI
    """
    list_display = ['hostname', 'business', 'idc', 'os', 'cpu', 'mem', 'disk', 'status', 'owner']


class BusiNessConfig(v1.AryaConfig):
    """
    自定义业务线展示UI
    """
    list_display = ['title']


v1.site.register(models.HostInfo, HostInfoConfig)
v1.site.register(models.BusiNess, BusiNessConfig)
