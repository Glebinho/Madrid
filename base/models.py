from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()
    #python manage.py makemigrations is used to detect the changes and store in a .py file
    #python manage.py applies the pending changes detected by makemigrations.

    def __str__(self):
        return self.name    #we are returning the name of a person.
    
