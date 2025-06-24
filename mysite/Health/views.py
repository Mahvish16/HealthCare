from django.shortcuts import render
from django.shortcuts import render
from .models import RegisterUser,Patient,Doctor
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer,PatientSerializer
from rest_framework.response import Response;
from rest_framework import status;
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404



# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        else:
            return Response({"message": "Invalid email or Password"}, status= status.HTTP_404_NOT_FOUND)

class PatientView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def post(self,request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        patient_id = kwargs.get('id')
        if patient_id:
            patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
            serializer = self.get_serializer(patient)
            return Response(serializer.data)
        else:
            patients = Patient.objects.filter(created_by=request.user)
            serializer = self.get_serializer(patients, many=True)
        return Response(serializer.data)
        
    def put(self, request, id, *args, **kwargs):
        patient = get_object_or_404(Patient, id=id, created_by=request.user)
        serializer = self.get_serializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id , *args, **kwargs):
        patient = get_object_or_404(Patient, id=id, created_by=request.user)
        patient.delete()
        return Response({"message": "Patient deleted successfully"}, status=status.HTTP_200_OK)




