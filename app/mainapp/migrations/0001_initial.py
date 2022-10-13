# Generated by Django 4.1.1 on 2022-10-09 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=45, unique=True, verbose_name="наименование"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="описание"
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="активна")),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "parent_id",
                    models.IntegerField(
                        blank=True, default=0, verbose_name="ID комментария"
                    ),
                ),
                ("comment", models.TextField(verbose_name="Комментарий")),
                (
                    "active",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="активна"
                    ),
                ),
                (
                    "delete",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="Удалена"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "коментарий",
                "verbose_name_plural": "коментарии",
            },
        ),
        migrations.CreateModel(
            name="CommentLikes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "like_count",
                    models.CharField(
                        choices=[("Like", "Like"), ("Dislike", "Dislike")],
                        max_length=10,
                        verbose_name="Лайки",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="активна"
                    ),
                ),
            ],
            options={
                "verbose_name": "Лайк к коментарию",
                "verbose_name_plural": "Лайки к коментариям",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=70, unique=True, verbose_name="Заголовок статьи"
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "active",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="активна"
                    ),
                ),
                (
                    "delete",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="Удалена"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=45, unique=True, verbose_name="наименование статуса"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус статьи",
                "verbose_name_plural": "Статусы статей",
            },
        ),
        migrations.CreateModel(
            name="PostLikes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "like_count",
                    models.CharField(
                        choices=[("Like", "Like"), ("Dislike", "Dislike")],
                        max_length=10,
                        verbose_name="Лайки",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="активна"
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.post",
                        verbose_name="Название статьи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лайк к статье",
                "verbose_name_plural": "Лайки к статьям",
            },
        ),
    ]