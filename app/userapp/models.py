from django.db import models
from django.contrib.auth.models import AbstractUser


class Skills(models.Model):
    # Модель скилов
    name = models.CharField(verbose_name='Название скила',  max_length=45)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Скилы'
        verbose_name_plural = 'Скилы'

    def __str__(self):
        return self.name


class User(AbstractUser):
    # Модель пользователя
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = ((MALE, 'М'), (FEMALE, 'Ж'),)
    username = models.CharField(verbose_name='Логин', blank=False, max_length=45, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', blank=True, max_length=45)
    first_name = models.CharField(verbose_name='Имя', blank=True, max_length=45)
    middle_name = models.CharField(verbose_name='Отчество', blank=True, max_length=45)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='user_avatar', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    phone_number = models.CharField(verbose_name='Телефон', blank=True, max_length=15)
    gender = models.CharField(verbose_name='Пол', max_length=6, blank=True, choices=GENDER_CHOICES)
    comments = models.TextField(verbose_name='O себе', blank=True, max_length=200)
    skills_id = models.ManyToManyField(Skills, verbose_name='Скилы', blank=True)
    delete = models.BooleanField(verbose_name='Удалена', default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(verbose_name='email', unique=True)
    is_email_verified = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def activate_user(self):
        self.is_active = True
        self.save()
