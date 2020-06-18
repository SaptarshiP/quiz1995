from django import forms

class login_credential(forms.Form):
    roll_number = forms.IntegerField(label="Roll Number")
    name_of_student = forms.CharField(label="Name",max_length=20)
    class_of_student = forms.CharField(label="Class",max_length=5)


