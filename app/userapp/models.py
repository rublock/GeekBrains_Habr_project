from django.db import models
from django.contrib.auth.models import AbstractUser


class Skills(models.Model):
    name = models.CharField(verbose_name='Название скила',  max_length=45)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Умение'
        verbose_name_plural = 'Умения'


class UserProfile(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = ((MALE, 'М'), (FEMALE, 'Ж'),)

    last_name = models.CharField(verbose_name='Фамилия', blank=True, max_length=45)
    first_name = models.CharField(verbose_name='Имя', blank=True, max_length=45)
    middle_name = models.CharField(verbose_name='Отчество', blank=True, max_length=45)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='user_avatar', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    phone_number = models.CharField(verbose_name='Телефон', blank=True, max_length=15)
    gender = models.CharField(verbose_name='Пол', max_length=6, blank=True, choices=GENDER_CHOICES)
    comments = models.TextField(verbose_name='O себе', blank=True, max_length=200)
    skills_id = models.ManyToManyField(Skills, verbose_name='Скилы')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def activate_user(self):
        self.is_active = True
        self.save()
