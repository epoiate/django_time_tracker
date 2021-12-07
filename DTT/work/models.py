from django.db import models

# Create your models here.


class WorkUnit(models.Model):

    activity = models.ForeignKey(to='activities.Activity', on_delete=models.CASCADE)
    worker = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()

