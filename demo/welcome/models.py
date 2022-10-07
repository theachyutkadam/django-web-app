from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=122)
  contact = models.CharField(max_length=10)
  desc = models.TextField()
  date = models.DateField()


  def __str__(self):
    return self.name
