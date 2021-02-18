from django.contrib import admin
from m2mapp.models import Student,Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','sname','email']
class CourseAdmin(admin.ModelAdmin):
    list_display = ['cno','cname','cfee']
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)

