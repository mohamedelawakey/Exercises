from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')\

products = Product.objects.prefetch_related('category')

# Practice Exercises
"""
Create a model representing a company with departments and employees, using ForeignKey relationships
Create a model for a product and its detailed description using a OneToOneField
Implement a ManyToManyField to model the relationship between students and courses
Explore different options for handling related object deletion in your models
Optimize queries involving complex relationships using prefetching and select_related
"""

class Company(models.Model):
    name = models.CharField(max_length=100)

class Departments(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

class Employees(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='employees')

class productt(models.Model):
    name = models.CharField(max_length=100)

class Description(models.Model):
    text = models.TextField()
    productt = models.OneToOneField(productt, on_delete=models.CASCADE, related_name='description')

class Courses(models.Model):
    title = models.CharField(max_length=100)

class Students(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Courses, related_name='students')

class Manager(models.Model):
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, related_name= 'teams', null= True)

employees = Employees.objects.select_related('department__company')
students = Students.objects.perfect_related('courses')
departments = Departments.objects.select_related('company').prefetch_related('employees')