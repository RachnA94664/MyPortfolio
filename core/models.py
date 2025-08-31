from django.db import models
from django.utils import timezone 
# Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # NEW
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



# Skill model
class Skill(models.Model):
    name = models.CharField(max_length=100)
    # removed percentage as per your request
    level = models.CharField(max_length=100, blank=True, null=True)  # Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name


# Certification model

class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)  # Use default date
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.provider}"


# core/models.py
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# core/models.py

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return "Profile Image"
