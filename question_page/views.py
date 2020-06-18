from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class question_page(TemplateView):
    template_name="question_page.html"