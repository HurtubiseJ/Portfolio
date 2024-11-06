from django.urls import path

from . import views
from .views import index_view, resume_view, about_view, projects_view

urlpatterns = [
    path("", index_view.as_view(), name="index"),
    path("resume/", resume_view.as_view(), name='resume'), 
    path('about/', about_view.as_view(), name='about'),
    path('projects/', projects_view.as_view(), name='projects'),
]