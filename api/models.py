from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    class Meta:
        abstract = True

class MentorProfile(UserProfile):
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    expertise = models.CharField(max_length=100)

class EntrepreneurProfile(UserProfile):
    company_name = models.CharField(max_length=100)