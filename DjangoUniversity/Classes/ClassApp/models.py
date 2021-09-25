from django.db import migrations, models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=100),
    Course_Number = models.IntegerField(null=True, blank=False),
    Instructor_Name = models.CharField(max_length=100),
    Duration = models.FloatField(min=0.0, max=10.0)

    objects = models.Manager()

    def __str__(self):
        return self.Title

    venvCourse = models.objects.create(Title="Venv", Course_Number=1, Instructor_Name="Mr. Kuykendall", Duration=2.5)
    modelCourse = models.objects.create(Title="Models", Course_Number=2, Instructor_Name="Ms. Quang", Duration=3.25)
    viewsCourse = models.objects.create(Title="Views", Course_Number=3, Instructor_Name="Mr. Kirkby", Duration=4)

    models.save()


