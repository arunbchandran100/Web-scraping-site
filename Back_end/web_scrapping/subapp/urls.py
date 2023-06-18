from django.contrib import admin
from django.urls import path
from .views import SubmitFormAPIView
urlpatterns = [

    path('form/', SubmitFormAPIView.as_view(), name='submit_form'),
]