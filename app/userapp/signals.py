from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from userapp.models import User
from django.contrib.auth.models import Group


@receiver(m2m_changed, sender=User.groups.through)
def add_remove_staff_if_user_moderator_or_not(
    sender, instance, action, reverse, model, pk_set, **kwargs
):
    if action in ("pre_add", "pre_remove"):
        if model.objects.filter(name="moderator").exists():
            moderator_gid = model.objects.filter(name="moderator").first().pk
            if moderator_gid in pk_set:
                if action == "pre_add":
                    instance.is_staff = True
                if action == "pre_remove":
                    instance.is_staff = False
    instance.save()
