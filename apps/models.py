from django.utils.timezone import now

from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.TextField(default='')
    phone = models.TextField(default='')
    password = models.TextField(default='')
    weight = models.FloatField(default=50)
    height = models.FloatField(default=5.5)
    bmi = models.FloatField()
    temp = models.FloatField(default=98)
    bp = models.FloatField()
    updated = models.DateTimeField(default=datetime.datetime.now())
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Prescription(models.Model):
    doc_name = models.CharField(max_length=200)
    hospital_name = models.CharField(max_length=100)
    image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.hospital_name


class Diabetes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_diabetes', null=True, blank=True)
    time = models.DateTimeField(default=now, editable=False)
    blood_sugar = models.FloatField()
    meal = models.IntegerField()
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.notes


class Medicine(models.Model):
    u_id = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    name = models.TextField()
    isMorning = models.BooleanField(default=False)
    isAfternoon = models.BooleanField(default=False)
    isNight = models.BooleanField(default=False)
    isMeal = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.name

