from django.contrib import admin
from django.urls import path
from new_project import views

urlpatterns = [
    path("" , views.index, name = 'new_project'),
    path("about" , views.about, name = 'about'),
    path("project" , views.project, name = 'project'),
    path("contact" , views.contact, name = 'contact'),
    path("test" , views.test, name = 'test'),
    
]
