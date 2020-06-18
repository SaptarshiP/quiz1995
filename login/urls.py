from django.urls import path
from login.views import retrieve_login_credential
urlpatterns = [
    path('login/',retrieve_login_credential.as_view()),
    #path('login/',get_data)

]