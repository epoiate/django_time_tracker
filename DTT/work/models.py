from django.db import models

# Create your models here.


class WorkUnit(models.Model):

    activity = models.ForeignKey(to='activities.Activity', on_delete=models.CASCADE)
    worker = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    date = models.ForeignKey(to='work.WorkDay', on_delete=models.CASCADE)
    duration = models.DurationField()


class WorkDay(models.Model):

    date = models.DateTimeField()


