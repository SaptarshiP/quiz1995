from django.shortcuts import render
from django.views.generic import TemplateView
from login.views import retrieve_login_credential
# Create your views here.
class HomeView(TemplateView):
    template_name='Home.html'
    def get(self,request):
        obj=retrieve_login_credential()
        name=obj.name
        return render(request,self.template_name,{'name':name})