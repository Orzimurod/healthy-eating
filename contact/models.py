from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    massage = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name
