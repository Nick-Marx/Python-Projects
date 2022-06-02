from django.db import models

# create a class and define fields to be stored in the db
class djangoClasses(models.Model):
    title = models.CharField(max_length=64, default="", blank=False, null=False)
    courseNumber = models.IntegerField(max_length=16, default="", blank=False, null=False)
    instructorName = models.CharField(max_length=32, default="", blank=False, null=False)
    duration = models.FloatField(max_length=64, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title
