from django.test import TestCase
from django.db import models

# Create your models here.
class Aluno(models.Model):
   nome = models.CharField(max_length=200)
   ra = models.CharField(max_length=7)
   email = models.CharField(max_length=200)
