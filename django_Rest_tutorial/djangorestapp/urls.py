
from django.urls import path
from djangorestapp.models import Article

from rest_framework.authtoken import views
 
 
from .views import *
app_name = 'restapi'
urlpatterns = [
         
         
        path('regi/',registerUser.some,name='some'),
        path('register/', registerUser.as_view(),name='register'),
        
        
        

]
