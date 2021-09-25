from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default='')
    course_Number = models.IntegerField(null=False, default=0)
    instructor_Name = models.CharField(max_length=100, default='')
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title
