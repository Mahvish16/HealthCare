from django.urls import path
from .views import RegisterView, LoginView,PatientView,DoctorView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/patients/', PatientView.as_view(), name='patient-list'),
    path('api/patients/<int:id>/', PatientView.as_view(), name='patient-detail'),
    path('api/doctors/', DoctorView.as_view(), name='doctor-list'),
    path('api/doctors/<int:id>/',DoctorView.as_view(), name='doctor-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]