from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.stu_home,name="stuhome"),
    path('assign/',views.assign_home,name="assign"),
    path('<poll_id>/',views.vote_it,name="vote"),
   

   
]