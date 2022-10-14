# Generated by Django 4.1.1 on 2022-10-14 18:31

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Название скила')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Скилы',
                'verbose_name_plural': 'Скилы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=45, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('last_name', models.CharField(blank=True, max_length=45, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=45, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=45, verbose_name='Отчество')),
                ('avatar', models.ImageField(blank=True, upload_to='user_avatar', verbose_name='Аватар')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=6, verbose_name='Пол')),
                ('comments', models.TextField(blank=True, max_length=200, verbose_name='O себе')),
                ('delete', models.BooleanField(db_index=True, default=False, verbose_name='Удалена')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('skills_id', models.ManyToManyField(blank=True, to='userapp.skills', verbose_name='Скилы')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
