from django.test import TestCase
from django.db import models

# Create your models here.
class app_aluno(models.Model):
   nome = models.CharField(max_length=200)
   ra = models.IntegerField(max_length=7)
   email = models.CharField(max_length=200)
