from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import login_credential
from .check_credential import check_login_credential
from django.forms import ModelForm
# Create your views here.
"""class display_it(TemplateView):
    template_name='login.html'
#class retrieve_data:
def get_data(request):
    if request.method=='POST':
        print("Hii I am here", request)
        form=login_credential(request.POST)
        print("form",form)
        if form.is_valid():
            data = form.cleaned_data['roll_number']
            print("data",data)
        #return HttpResponse("Pampashyamal")
    #return HttpResponse("pampashyamalget")
    return render(request,"login.html")"""
class retrieve_login_credential(TemplateView):
    template_name = "login.html"
    form_class=login_credential
    name="Pampashyamal"
    applicant_roll_number=0
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        obj=check_login_credential()
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            data_got=form_data.cleaned_data['roll_number']
            print("data_got",data_got)
            credential_result=obj.check_it(form_data)
            if credential_result=="The student is registered":
                retrieve_login_credential.name=form_data.cleaned_data['name_of_student']
                retrieve_login_credential.applicant_roll_number=form_data.cleaned_data['roll_number']
                return HttpResponseRedirect('/home/')
            else:
                form=self.form_class()
                return render(request,self.template_name,{'form':form})