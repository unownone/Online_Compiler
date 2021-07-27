from django.contrib import admin
from django.urls import path,include
from . import views as view

urlpatterns=[
    path('compile',view.compileCode,name="Submit form"),
    path('',view.code_form, name="ONLINE COMPILER"),
]