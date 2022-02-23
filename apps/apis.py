from rest_framework import request, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

from apps import helpers, models
from apps.serializers import *
from common.apis import FullViewSet


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'retrieve', 'put', 'patch']

    def obj_filter(self, request):
        return helpers.user_filter(self, request)


class PrescriptionViewSet(FullViewSet):
    permission_classes = (AllowAny,)
    ObjModel = Prescription
    ObjSerializer = PrescriptionSerializer

    def obj_filter(self, request):
        return helpers.prescription_filter(self, request)


class DiabetesViewSet(FullViewSet):
    permission_classes = (AllowAny,)
    ObjModel = Diabetes
    ObjSerializer = DiabetesSerializer

    def obj_filter(self, request):
        return helpers.diabetes_filter(self, request)


class MedicineViewSet(FullViewSet):
    permission_classes = (AllowAny,)
    ObjModel = Medicine
    ObjSerializer = MedicineSerializer

    def obj_filter(self, request):
        return helpers.medicine_filter(self, request)



