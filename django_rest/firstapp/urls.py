from django import views
from django.urls import path
from .views import student_details
# from .views import *
urlpatterns = [
    path('students/',views.student_details, name='student'),
    # path('register',UserRegisterView.as_view()),
]
