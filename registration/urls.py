from django.urls import path
from .views import retrieve_registration_credential

urlpatterns = [
    path('',retrieve_registration_credential.as_view())
]