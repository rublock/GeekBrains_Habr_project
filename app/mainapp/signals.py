from django.db.models.signals import pre_delete

from .models import Post


@receceiver(pre_delete, sender=Post)
def set_deleted(sender, instance):
    instance.is_deleted = True
    instance.save()
