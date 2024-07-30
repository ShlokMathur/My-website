from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    
    email = models.CharField(max_length = 122)
    country = models.CharField(max_length = 122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
         return self.firstName + " " + self.lastName
