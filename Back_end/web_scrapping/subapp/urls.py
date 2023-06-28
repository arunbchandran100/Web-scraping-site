from django.contrib import admin
from django.urls import path
from .views import SubmitFormAPIView
from .views import product_data
from . import views
urlpatterns = [

    path('form/', SubmitFormAPIView.as_view(), name='submit_form'),
    #path('product/', views.apicall_99acres),
    #path('product/', FetchData.as_view(), name='func_data'),
]