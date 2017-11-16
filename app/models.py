from django.test import TestCase
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Curso(models.Model):
      sigla = models.CharField(max_length=5)
      nome = models.CharField(max_length=200)

      def __str__(self):
            return self.nome

class UsuarioManager(BaseUserManager):
      use_in_migrations = True
      def _create_user(self, ra, password, **extra_fields):
          if not ra:
              raise ValueError('RA precisa ser preenchido')
          user = self.model(ra=ra, **extra_fields)
          user.set_password(password)
          user.save(using=self._db)
          return user
      def create_user(self, ra, password=None, **extra_fields):
          return self._create_user(ra, password, **extra_fields)
      def create_superuser(self, ra, password, **extra_fields):
          return self._create_user(ra, password, **extra_fields)
