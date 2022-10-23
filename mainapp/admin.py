from django.contrib import admin

# Register your models here.
from mainapp.models import News, Course, Lesson, CourseTeacher

admin.site.register(News)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseTeacher)