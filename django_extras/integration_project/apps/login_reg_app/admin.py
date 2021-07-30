from django.contrib import admin
from ..login_reg_app.models import User
from ..courses_app.models import Course
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)