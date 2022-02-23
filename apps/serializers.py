from common.serializers import CustomSerializer

from apps.models import *
from rest_framework import serializers


class DiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diabetes
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    user_diabetes = DiabetesSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user_hobby = validated_data.pop('user_diabetes')
        profile_instance = User.objects.create(**validated_data)
        for hobby in user_hobby:
            Diabetes.objects.create(user=profile_instance, **hobby)
        return profile_instance


class PrescriptionSerializer(CustomSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
