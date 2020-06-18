from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import registration_form
from login.forms import login_credential
# Create your views here.
class retrieve_registration_credential(TemplateView):
    template_name = "registration.html"
    template_name2= "login.html"
    form_name=registration_form
    form_name2=login_credential
    def get(self,request):
        form=self.form_name()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        registration_data=self.form_name(request.POST)
        if registration_data.is_valid():
            name = registration_data.cleaned_data['student_name']
            print("name",name)
            form = self.form_name2()
            registration_data.save()
            return render(request,self.template_name2,{'form':form})
        form=self.form_name()

        return render(request,self.template_name,{'form':form})