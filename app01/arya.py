#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/23

from arya.service import v1
from . import models


# 自定义一些属性
class UserInfoConfig(v1.AryaConfig):
    """
    自定义用户信息UI
    """
    list_display = ['username', 'ut', 'roles', 'email']


class UserTypeConfig(v1.AryaConfig):
    """
    自定义用户类型UI
    """
    list_display = ['title']


class RoleConfig(v1.AryaConfig):
    """
    自定义角色UI
    """
    list_display = ['caption']


v1.site.register(models.UserInfo, UserInfoConfig)
v1.site.register(models.UserType, UserTypeConfig)
v1.site.register(models.Role, RoleConfig)
