from django.db import models

# Create your models here.


class Client(models.Model):

    name = models.CharField(verbose_name="Client's name", max_length=255, blank=True)
