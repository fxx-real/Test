from .models import CityDict, CourseOrg, Teacher

import xadmin

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'city', 'location', 'image', 'desc', 'address', 'click_nums', 'fav_nums', 'index', 'add_time']
    search_fields = ['name', 'city', 'location', 'image', 'desc', 'address', 'click_nums', 'fav_nums', 'index']
    list_filter = ['name', 'city', 'location', 'image', 'desc', 'address', 'click_nums', 'fav_nums', 'index', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'feathers', 'add_time',
                     'click_nums', 'fav_nums']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'feathers',
                     'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'feathers', 'add_time',
                     'click_nums', 'fav_nums']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
