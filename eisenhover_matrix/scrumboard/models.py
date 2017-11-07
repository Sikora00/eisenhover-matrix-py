from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.TextField()

    def __str__(self):
        return "Task : {}".format(self.title)
