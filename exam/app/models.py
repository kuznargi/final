
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Book (models.Model):
    Image=models.ImageField(upload_to='book/')
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=20)
    description=models.TextField()

# class Collage(models.Model):
#     name=models.CharField(max_length=20)
#     address=models.CharField(max_length=20)
#     phoneNumber=models.CharField(max_length=20)
#     website=models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name}"
class Group(models.Model):
    name=models.CharField(max_length=20)
    studyLanguage=models.CharField(max_length=20)

class CustomUser(AbstractUser):
    
    class Gender(models.TextChoices):
        Man = 'Man'
        Woman =  'Woman'  
    class Status(models.TextChoices):
        Student =  'Student'
        Teacher =   'Teacher'  

    Image=models.ImageField(upload_to='user/',default="user/default.png")
    gender=models.CharField(max_length=10,choices=Gender.choices,default=Gender.Man)
    phone=models.CharField(max_length=20)
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.Student) 
   
    # content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, default=1)
    # object_id = models.PositiveIntegerField(default=1)
    # content_object = GenericForeignKey('content_type', 'object_id')

    # college=models.ManyToManyField(Collage)
    
    def __str__(self):
        return f"{self.first_name} {self.status}"
class Subject(models.Model):
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'status': CustomUser.Status.Teacher}
    )
    name = models.CharField(max_length=20)
    hours = models.IntegerField()

class HomeWork(models.Model):
    Image = models.ImageField(upload_to='homework/',null=True,blank=True)
    Title = models.CharField(max_length=20,null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,blank=True)  # Reference the Subject model
    StudentComment = models.TextField(null=True,blank=True)
    Mark = models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    homework = models.FileField(upload_to="homework",null=True,blank=True)





# class Student(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='students')
#     group=models.CharField(max_length=20)
#     departpent=models.CharField(max_length=20)
# class Teacher(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teachers')
#     position=models.CharField(max_length=20)

