#-*- coding:utf-8 -*-

from django.conf.urls import url, include

from .views import OrgList, AddUserAskView, DetailHomeView, OrgCourseView, AddFavView

urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgList.as_view(), name="orglist"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^detail_homepage/(?P<org_id>\d+)', DetailHomeView.as_view(), name="detail_home"),
    url(r'^course/(?P<org_id>\d+)', OrgCourseView.as_view(), name="detial_course"),
    url(r'^addfav/$', AddFavView.as_view(), name="add_fav"),
]