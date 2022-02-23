from rest_framework.response import Response

from apps.models import *


def user_filter(self, request):
    return User.objects.all()


def prescription_filter(self, request):
    return Prescription.objects.all()


def diabetes_filter(self, request):
    return Diabetes.objects.all()


def medicine_filter(self, request):
    return Medicine.objects.all()


