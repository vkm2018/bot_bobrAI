from enum import unique

from django.db import models

# Create your models here.

class ProfileTelegram(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

class InfoBot(models.Model):
    profile = models.ForeignKey(ProfileTelegram, on_delete=models.CASCADE)
    created_ad = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=255, verbose_name='Город')
    current_temp = models.CharField(max_length=255, verbose_name='Текущая температра')
    feels = models.CharField(max_length=255, verbose_name='Ощущаемая температура')
    desc = models.CharField(max_length=255, verbose_name='Описание')
    hum = models.CharField(max_length=255,verbose_name='Влажность')
    wind = models.CharField(max_length=255, verbose_name='Скорость ветра')

    def __str__(self):
        return self.city

class CommandBot(models.Model):
    profile = models.ForeignKey(ProfileTelegram, on_delete=models.PROTECT)
    command = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.profile}{self.command}'