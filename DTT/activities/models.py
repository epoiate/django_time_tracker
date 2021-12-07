from django.db import models

# Create your models here.


class Activity(models.Model):

    project = models.ForeignKey(to='projects.Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)


