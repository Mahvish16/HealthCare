from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

gender =(
    ('male', 'male'),
    ('female', 'female'),
    ('others','others')
)

# Create your models here.
class RegisterUserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,email,password = None):
        user = self.create_user(name=name, email=email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class RegisterUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = RegisterUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    address = models.TextField(max_length = 100)
    created_by =models.ForeignKey(RegisterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Doctor(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    specialist = models.CharField(max_length=50)
    phone_number =models.IntegerField()
    created_by =models.ForeignKey(RegisterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    
class PatientDoctorMapping(models.Model):
    patient = models.ManyToManyField(Patient)
    doctor = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.patient.email
    


    

    


