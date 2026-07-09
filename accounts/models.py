from django.db import models
from django.contrib.auth.models import User


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name