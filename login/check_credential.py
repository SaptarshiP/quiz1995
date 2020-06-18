from registration.models import registration

class check_login_credential:
    def check_it(self,form_data):
        p = registration.objects.filter(student_roll_number=form_data.cleaned_data['roll_number'],student_name=form_data.cleaned_data['name_of_student'],student_class=form_data.cleaned_data['class_of_student'])
        try:
            print("Data received",p[0].student_name)
            return "The student is registered"
        except:
            print("the exception occured")
            return "The student is not registered"