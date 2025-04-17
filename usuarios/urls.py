from django.urls import path
from .views import RegisterView, ProtectedView  # 👈 Agregás ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protected/', ProtectedView.as_view(), name='protected'),  # 👈 Nueva ruta protegida
]
