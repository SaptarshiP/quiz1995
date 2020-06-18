from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .question_get import question_manipulation

# Create your views here.
def get_data(request):
    #if request.Method=='GET':
    obj=question_manipulation()
    data_got=obj.retrieve_all_the_question()
    serialized_data=serializers.serialize('json',data_got)
    return JsonResponse(serialized_data,safe=False)
    # else:
    #     return HttpResponse("Nothing to post")