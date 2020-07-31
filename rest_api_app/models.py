from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(unique=True, max_length=16)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.username
    

