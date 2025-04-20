from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Grupo
from .serializers import RegisterSerializer, GrupoSerializer, PermisoSerializer
from django.contrib.auth.models import Permission

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegisterSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]

class PermisoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [IsAuthenticated]
