from django.db import models
from django.conf import settings


class Category(models.Model):
    # Модель категорий
    name = models.CharField(max_length=45, verbose_name='наименование')
    description = models.CharField(max_length=300, blank=True, verbose_name='описание')
    active = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return f'{self.name}{"" if self.active else "(блок)"}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Status(models.Model):
    # Модель статусы статьи
    name = models.CharField(max_length=45, verbose_name='наименование статуса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус статьи'
        verbose_name_plural = 'Статусы статей'


class Post(models.Model):
    # Модель статьей
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок статьи', max_length=70)
    description = models.TextField(verbose_name='Описание')
    category_id = models.ForeignKey(Category, verbose_name='Категории статей', on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name='активна', default=True, db_index=True)
    delete = models.BooleanField(verbose_name='Удалена', default=False, db_index=True)
    # status_id = models.ForeignKey(Status, verbose_name='Статусы статьи', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}{"" if self.active else "(блок)"}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Comment(models.Model):
    # Модель комментариев
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE)
    parent_id = models.IntegerField( verbose_name='ID комментария')
    post_id = models.ForeignKey(Post, verbose_name='Название статьи', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')
    active = models.BooleanField(verbose_name='активна', default=True, db_index=True)
    delete = models.BooleanField(verbose_name='Удалена', default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'
