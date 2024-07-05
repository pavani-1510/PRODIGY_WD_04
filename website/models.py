# website/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name
