from django.core.management.base import BaseCommand
from django.utils import timezone

from userapp.models import User
from config.settings import EMAIL_HOST_USER


class Command(BaseCommand):
    help = (
        "Создание администратора (логин и пароль admin, ОБЯЗАТЕЛЬНО сменить пароль!!!)"
    )

    def handle(self, *args, **kwargs):
        admin, created = User.objects.get_or_create(
            username="admin",
            is_staff=True,
            is_superuser=True,
        )
        if created:
            admin.set_password("admin")
            admin.is_email_verified = True
            admin.is_active = True
            admin.save()
