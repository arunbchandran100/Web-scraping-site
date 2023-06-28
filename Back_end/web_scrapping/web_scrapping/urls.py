
from django.contrib import admin
from django.urls import path,include
from subapp import views
#from subapp.views import FetchData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subapp/',include('subapp.urls')),
    #path('product/', views.apicall_squareyards),
    #path('product/', views.apicall_99acres),
    #path('product/', views.apicall_nobroker),
    #path('/product/<str:city>/<str:locality>/', views.apicall_squareyards),
    #path('product/', FetchData.as_view(), name='func_data'),

    path('product/', views.aggregate_api_calls),

]