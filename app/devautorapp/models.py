from django.db import models


class DevAuthor(models.Model):
    # Модель Авторов

    last_name = models.CharField(verbose_name="Фамилия", blank=True, max_length=45)
    first_name = models.CharField(verbose_name="Имя", blank=True, max_length=45)
    middle_name = models.CharField(verbose_name="Отчество", blank=True, max_length=45)
    avatar = models.ImageField(
        default="user.png",
        null=True,
        verbose_name="Аватар",
        upload_to="user_avatar",
        blank=True,
    )
    birthday = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    comments = models.TextField(verbose_name="O себе", blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gb = models.URLField(verbose_name="GeekBrains", unique=True)
    telegramm = models.URLField(verbose_name="Telegramm", unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Автор проекта"
        verbose_name_plural = "Авторы проекта"

    def activate_user(self):
        self.is_active = True
        self.save()
