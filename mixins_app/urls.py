from django.conf.urls import url
from django.urls import path

from .views import Teacherlist,Teacherdetails,Studentlist,Studentdeails,Attendedetails,Attendeclist

urlpatterns=[
    path('teacher/',Teacherlist.as_view()),
    path('teacher/<int:pk>/',Teacherdetails.as_view()),
    path('student/',Studentlist.as_view()),
    path('student/<str:pk>/',Studentdeails.as_view()),
    path('atd/',Attendeclist.as_view()),
    path('atd/<int:pk>/',Attendedetails.as_view())

]