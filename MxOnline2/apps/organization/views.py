# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm
from courses.models import Course
from users.models import UserFav

class OrgList(View):
    def get(self, request):
        #课程机构
        all_orgs = CourseOrg.objects.all()
        #城市
        all_citys =CityDict.objects.all()
        #点击数
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        #筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        #类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        org_nums = all_orgs.count()
        #排序
        order_type = request.GET.get('sort', "")
        if order_type == "students":
            all_orgs = all_orgs.order_by("-students")
        elif order_type == "courses":
            all_orgs = all_orgs.order_by("-course_nums")
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs,5, request=request)

        orgs = p.page(page)

        return render(request, "html/org-list.html",{
            "all_orgs" : orgs,
            "all_city":all_citys,
            "city_id":city_id,
            "category":category,
            "org_nums":org_nums,
            "hot_orgs":hot_orgs,
            "order_type":order_type
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')

class DetailHomeView(View):
    def get(self, request, org_id):
        org = CourseOrg.objects.get(id = int(org_id))
        #通过Course的外键反向取到所有 以这个机构为外键的课程
        all_courses = org.course_set.all()[:3]
        all_teacher = org.teacher_set.all()[:1]
        return render(request, "html/org-detail-homepage.html", {
            'all_courses':all_courses,
            'all_teacher':all_teacher,
            'org':org
        })


class OrgCourseView(View):
    """
    机构课程列表页
    """
    def get(self, request, org_id):
        org = CourseOrg.objects.get(id=int(org_id))
        # 通过Course的外键反向取到所有 以这个机构为外键的课程
        all_courses = org.course_set.all()
        return render(request, "html/org-detail-course.html", {
            'all_courses': all_courses,
            'org': org
        })


class AddFavView(View):
    def post(self,request):
        fav_id = request.POST.get("fav_id",0)
        fav_type = request.POST.get("fav_type", 0)

        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail" , "msg":"用户未登录"}', content_type='application/json')

        exist_record = UserFav.objects.get(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_record:
            exist_record.delete()
            return HttpResponse('{"status":"success" , "msg":"收藏"}', content_type='application/json')
        else:
            if fav_id>0 and fav_type>0:
                user_fav = UserFav()
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success" , "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail" , "msg":"收藏出错"}', content_type='application/json')

