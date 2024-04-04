from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    specialization = models.ManyToManyField(Specialization, verbose_name='Специализация')
    address = models.CharField(max_length=256, verbose_name='Адресс')
    website = models.CharField(max_length=256, verbose_name='Веб-сайт')
    phone = models.CharField(max_length=32, verbose_name='Телефон')

    def __str__(self):
        return self.name