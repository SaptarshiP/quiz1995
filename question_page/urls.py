from django.urls import path
from .views import question_page
urlpatterns=[
    path('',question_page.as_view())
]