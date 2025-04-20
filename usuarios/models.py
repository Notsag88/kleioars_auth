from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    permisos_individuales = models.ManyToManyField(Permission, blank=True)

    def get_all_permissions(self):
        permisos = set(self.permisos_individuales.all())
        for grupo in self.grupos.all():
            permisos |= grupo.get_all_permissions()
        return permisos

class Grupo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    permisos = models.ManyToManyField(Permission, blank=True)
    usuarios = models.ManyToManyField(Usuario, related_name='grupos', blank=True)
    subgrupos = models.ManyToManyField('self', symmetrical=False, related_name='supergrupos', blank=True)

    def __str__(self):
        return self.nombre

    def get_all_permissions(self):
        permisos = set(self.permisos.all())
        for subgrupo in self.subgrupos.all():
            permisos |= subgrupo.get_all_permissions()
        return permisos
