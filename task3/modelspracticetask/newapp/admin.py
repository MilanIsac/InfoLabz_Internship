from django.contrib import admin
from .models import Student, Course, Instructor

# Register your models here.

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'price', 'dateOfBirth', 'contact', 'email')
    
@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_code', 'price', 'start_date', 'end_date', 'is_available')
    
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact', 'department', 'date_of_joining', 'date_of_birth', 'is_active', 'linkedin_url')