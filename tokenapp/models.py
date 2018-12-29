from django.db import models
import datetime


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    worker_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return (str(self.id) + " " + self.worker_name)


class Attendence(models.Model):
    Date = models.DateField(default=datetime.datetime.today)
    attendence_string = models.TextField(blank=True)

    def __str__(self):
        return (str(self.id) + " " + self.worker_name)
