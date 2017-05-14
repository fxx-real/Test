from django.conf.urls import include, url

from .views import CourseList, CourseDetail

urlpatterns = [
    url(r'^list/$', CourseList.as_view(), name="course_list"),
    url(r'^course_detial/(?P<course_id>\d+)$', CourseDetail.as_view(), name="course_detial")
]
