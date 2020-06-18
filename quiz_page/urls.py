from django.urls import path
from .views import get_data
from django.views.generic import View
urlpatterns=[
    path('',get_data)
    #path('',quiz_page_display.as_view())
]