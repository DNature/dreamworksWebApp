from django.contrib import admin
from .models import Course_Category, Course_Materials

# Register your models here.

admin.site.register(Course_Category)

@admin.register(Course_Materials)
class Course_Material_Admin(admin.ModelAdmin):
    list_display = ('title', 'category', 'course_type', 'download_link', 'latest')
    list_filter = ('title', 'category')
