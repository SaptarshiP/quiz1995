from django import forms
from .models import registration
class registration_form(forms.ModelForm):
    student_roll_number = forms.IntegerField(label="Roll Number")
    student_name = forms.CharField(label="Name",max_length=20)
    student_class = forms.CharField(label="Class",max_length=5)
    student_section = forms.CharField(label="Section",max_length=5)
    student_mother_name = forms.CharField(label="Mother Name",max_length=20)
    student_father_name = forms.CharField(label="Father Name",max_length=20)
    student_address = forms.CharField(label="Address",max_length=50)
    class Meta:
        model=registration
        fields =['student_roll_number','student_name','student_class','student_section','student_mother_name','student_father_name','student_address']