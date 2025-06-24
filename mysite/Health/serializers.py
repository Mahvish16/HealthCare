from rest_framework import serializers
from .models import RegisterUser,Patient,Doctor

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = RegisterUser
        fields = ('name', 'email', 'password')
    def create(self,validated_data):
        user = RegisterUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name', 'email', 'address')
    def create(self, validated_data):
        user = self.context['request'].user
        patient = Patient.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            address=validated_data['address'],
            created_by =user
        )
        return patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('first_name','last_name', 'email','specialist', 'phone_number', )
