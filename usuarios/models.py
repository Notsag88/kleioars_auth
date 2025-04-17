from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    es_docente = models.BooleanField(default=False)
    es_alumno = models.BooleanField(default=False)
