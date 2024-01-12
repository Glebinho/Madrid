from django.db import models

# Create your models here.

class Shape(models.Model):
    photo = models.ImageField(upload_to="static/", verbose_name="Фото")
    title = models.CharField(max_length=150, verbose_name="Название формы")
    Price = models.IntegerField(blank=True, verbose_name="Цена")
class Contact(models.Model):
    name = models.TextField()
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
        #python manage.py makemigrations is used to detect the changes and store in a .py file
    #python manage.py applies the pending changes detected by makemigrations.
EDUCATION_TYPE = (
    ('1', 'Домашняя футболка'),
    ('2', 'Гостевая футболка'),
    ('3', 'Особая футболка')
    )
EDUCATION = (
    ('1', 'S'),
    ('2', 'M'),
    ('3', 'L'),
    ('4', 'XL')
    )
class History(models.Model):
    tovar = models.CharField(max_length=30, verbose_name="goods", choices=EDUCATION_TYPE)
    razmer = models.CharField(max_length=30, verbose_name="size", choices=EDUCATION)
    kol = models.CharField(max_length=30, verbose_name="quantity goods")
    email = models.CharField(max_length=30, verbose_name="@email")
    fio = models.CharField(max_length=30, verbose_name="FIO")
    date = models.DateField(verbose_name="data")
    text = models.TextField(verbose_name="adress")

class Meta:
    verbose_name = 'История заказов'
    verbose_name_plural = 'История заказов'

    #we are returning the name of a person.
    
