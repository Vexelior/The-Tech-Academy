from django.db import models

# Our class to outline our objects attributes.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField()
    instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.title

