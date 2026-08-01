from django.db import models

class ModelMixin(models.Model):
    name =models.CharField(max_length=30)
    roll =models.IntegerField()
    department = models.CharField(max_length=40)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
