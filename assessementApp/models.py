from django.db import models

# Create your models here.

from django.db import models
from django.forms import CharField 

 
class staticIndexNumbers(models.Model):
  Student_IndexNumber=models.CharField(max_length=10)
  def __str__(self):
     return self.Student_IndexNumber


class Announcement(models.Model):
   title=models.CharField(max_length=200)
   message=models.TextField()
   date=models.DateTimeField()

   def __str__(self):
    return self.title 
    

class absenceReport(models.Model):
   Student_Name=models.CharField(max_length=100)
   Student_Class=models.CharField(max_length=40)
   Parent_Name=models.CharField(max_length=100)
   reason=models.TextField()
   proveFile=models.FileField(upload_to='upload', blank=True, null=True) 
   submitted_date=models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.Parent_Name 


class studentLogin(models.Model):
   password=models.CharField(max_length=50)  
   indexnumber=models.CharField(max_length=10)

class Assess_Student(models.Model): 
    index_Number = models.CharField(max_length=10)   
    Total_Quiz_Marks = models.FloatField()
    Total_Assignment_Mark = models.FloatField()
    Attendance_Mark= models.FloatField() 
    Mid_Sem=models.FloatField()
    Total=models.FloatField(null=True, blank=True) 
     
    def __str__(self):
        return self.index_Number 


# Student Result model
class studentResult(models.Model):
   index_number=models.CharField(max_length=10)
   Quizzes= models.IntegerField(default=0, editable=False)
   Assignments=models.IntegerField(default=0, editable=False)
   
# Form Master model
class FormMaster(models.Model):
   name=models.CharField(max_length=100)
   ClassHanlder =models.CharField(max_length=100)
   phoneNumber= models.IntegerField( )
   age=models.IntegerField() 
   picture= models.ImageField(blank=True, null=True)
   
 
#  Headmaster model
class  Headmaster(models.Model):
   name=models.CharField(max_length=50)
   phoneNumber=models.IntegerField( )
   email=models.EmailField()
   picture=models.ImageField( blank=True, null=True) 
   