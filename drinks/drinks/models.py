from django.db import models

class malik(models.Model):
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    drink=models.CharField(max_length=20)

    def __str__(self):
        return self.name


