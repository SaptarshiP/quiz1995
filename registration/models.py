from django.db import models

# Create your models here.
class registration(models.Model):
    student_roll_number = models.IntegerField()
    student_name = models.CharField(max_length=20)
    student_class = models.CharField(max_length=5)
    student_section = models.CharField(max_length=5)
    student_mother_name = models.CharField(max_length=20)
    student_father_name = models.CharField(max_length=20)
    student_address = models.CharField(max_length=50)