from django.db import models

# Create your models here.
class question_bank(models.Model):
    question_number = models.IntegerField()
    question = models.CharField(max_length=400)
    correct_answer = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100,null=True)