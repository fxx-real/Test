#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length = 50 , verbose_name=u"昵称" , default="")
    birthday = models.DateField(max_length=5,verbose_name=u"生日" , null=True , blank=True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default = "female")
    address = models.CharField(max_length=100 , default="")
    mobile = models.CharField(max_length=11 , null=True , blank=True)
    image = models.ImageField(max_length=100,upload_to="image/%Y/%m",default=u"image/default.png")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20 , verbose_name=u"验证码")
    email = models.EmailField(max_length=50 , verbose_name=u"邮箱")
    send_type = models.CharField(max_length=20, choices=(("register","注册"),("forget",u"忘记密码")), verbose_name=u"传输类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"传输时间")#如果now后面加括号的话生成的是编译时的时间，去掉括号才是实例化时的时间

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length = 100 , verbose_name= u"标题")
    image = models.ImageField(max_length=100 , upload_to = "banner/%Y/%m" , verbose_name=u"轮播图")
    url = models.URLField(max_length=200 , verbose_name=u"访问地址")
    index = models.IntegerField(default=100 , verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now , verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

class UserFav(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户id")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"机构"),(3,"教师")))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name