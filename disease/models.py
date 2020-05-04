from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    PATIENT = 1
    DOCTOR = 2
    HOSPITAL = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (HOSPITAL, 'Hospital'),
        (ADMIN, 'Admin'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class City(models.Model):
    name = models.CharField(max_length = 30)

    class Meta:
        verbose_name = "Citie"

    def __str__(self):
        return self.name

class Symptoms(models.Model):
    name = models.CharField(max_length = 30)

    class Meta:
        verbose_name = "Symptom"
        # ordering = ["name"]

    def __str__(self):
        return self.name
