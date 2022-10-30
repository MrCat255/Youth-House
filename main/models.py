from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from phonenumber_field.modelfields import PhoneNumberField

from YouthHouseBackend import settings


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    username = models.CharField(max_length=30, verbose_name='Никнейм')
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='static/user/images/', blank=True, verbose_name='Аватарка')
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, verbose_name='Номер телефона')
    gender = models.BooleanField(null=True, default=None, verbose_name='Пол')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    about_me = models.TextField(null=True, blank=True, max_length=250, verbose_name='О себе')

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'


class Applications(models.Model):
    name = models.TextField(verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    tel = models.TextField(verbose_name="Tel", null=True, blank=True)
    date = models.DateTimeField(verbose_name="Время", null=True, blank=True)
    hall = models.IntegerField(verbose_name="Номер зала", null=True, blank=True)
    accepted = models.BooleanField(verbose_name="Принято", default=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # if not self.pk:
        print('save123')
        super(Applications, self).save(*args, **kwargs)

        email = 's.skorobogatov.d@yandex.ru'

        msg_html = render_to_string('new_application.html', context={'id': self.id, 'name': self.name, 'date': self.date, 'tel': self.tel, 'email': self.email})
        mail = send_mail('код подтверждения', '', settings.EMAIL_HOST_USER, [email], fail_silently=False,
                         html_message=msg_html, )

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
