from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Post


@receiver(pre_delete, sender=Post)
def set_deleted(sender, instance):
    instance.is_deleted = True
    instance.save()
