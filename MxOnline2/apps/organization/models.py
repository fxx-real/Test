#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"城市"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    location = models.CharField(max_length=50, verbose_name=u"通讯详细地址")
    image = models.ImageField(max_length=100, upload_to="org/%Y/%m", verbose_name=u"封面图")
    desc = models.TextField(verbose_name=u"机构描述")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    category = models.CharField(max_length=50, choices= (("pxjg","培训机构"),("gx","高校"),("gr","个人")),verbose_name=u"机构类型",null=True)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    index = models.IntegerField(default=999, verbose_name=u"排序")
    add_time = models.DateField(default=datetime.now)


    class Meta:
        verbose_name=u"课程机构"
        verbose_name_plural = verbose_name

    def getTeacherNum(self):
        return self.teacher_set.all().count()

    def getCouseNum(self):
        return self.course_set.all().count()
    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position= models.CharField(max_length=50, verbose_name=u"公司职位")
    feathers = models.CharField(max_length=50, verbose_name=u"教学特点")
    add_time = models.DateField(default=datetime.now)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")

    class Meta:
        verbose_name=u"教师"
        verbose_name_plural = verbose_name

class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名称")
    add_time = models.DateTimeField(default= datetime.now, verbose_name=u"提交时间")


    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name