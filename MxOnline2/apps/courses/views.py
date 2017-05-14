#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class CourseList(View):
    def get(self, request):
        all_course = Course.objects.order_by("-add_time")
        #排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-students")
            elif sort == "hot":
                all_course = all_course.order_by("-click_nums")
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course,6, request=request)

        all_course = p.page(page)

        return render(request, "html/course-list.html",{
            "all_course":all_course,
            "sort":sort
        })

class CourseDetail(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, "html/course-detail.html", {
            "course":course
        })