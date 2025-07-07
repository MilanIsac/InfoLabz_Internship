from django.db import models

# Create your models here.

courses = [
    ('python', 'Python'),
    ('flutter', 'Flutter'),
    ('django', 'Django'),
    ('react', 'React'),
    ('php', 'PHP'),
]

departments =[
    ('sales', 'Sales'),
    ('marketing', 'Marketing'),
    ('development', 'Development'),
    ('hr', 'HR'),
]


class Student(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dateOfBirth = models.DateField(verbose_name="Birth Date")
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    
class Course(models.Model):
    course_title = models.CharField(max_length=100, choices=courses)
    course_code = models.CharField(verbose_name="Course Code", max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Course Description")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    is_available = models.BooleanField(default=True, verbose_name='Active Status')


class Instructor(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    department = models.CharField(choices=departments, max_length=50)
    date_of_joining = models.DateField(verbose_name="Date of Joining")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    is_active = models.BooleanField(default=True, verbose_name='Active Status')
    linkedin_url = models.URLField(verbose_name="LinkedIn Profile")