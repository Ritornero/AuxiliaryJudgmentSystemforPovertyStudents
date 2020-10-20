from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=125, verbose_name='登录密码')
    profession = models.CharField(max_length=125, verbose_name='职业')
    phone = models.CharField(max_length=128, verbose_name='电话')

    def __str__(self):
        return '<User: {}>'.format(self.username)
