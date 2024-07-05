# website/views.py

from django.shortcuts import render
from .models import Project, Skill, AboutMe

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    about_me = AboutMe.objects.first()
    return render(request, 'home.html', {'projects': projects, 'skills': skills, 'about_me': about_me})
