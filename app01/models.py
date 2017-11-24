from django.db import models


class UserType(models.Model):
    """
    用户类型表
    """
    title = models.CharField(max_length=32, verbose_name="用户类型")

    class Meta:
        verbose_name_plural = "用户类型表"

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    caption = models.CharField(max_length=32, verbose_name="角色名")

    class Meta:
        verbose_name_plural = "角色表"

    def __str__(self):
        return self.caption


class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    email = models.CharField(max_length=32, verbose_name="邮箱")
    ut = models.ForeignKey(to="UserType", blank=True, verbose_name="用户类型")
    roles = models.ManyToManyField(to="Role", blank=True, verbose_name="所属角色")

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.username
