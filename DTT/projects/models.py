from django.db import models


# Create your models here.


class Project(models.Model):

    client = models.ForeignKey(to='clients.Client', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

