from django.contrib.auth.models import Group
from django.db import migrations


def add_group_permissions(apps, schema_editor):
    group, created = Group.objects.get_or_create(name="moderator")
    group.permissions.set([33,34,35,36]) # Права на модерацию статей
    group.permissions.set([25,26,27,28]) # Права на модерацию комментов


class Migration(migrations.Migration):
    dependencies = [
        ('userapp', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_group_permissions),
    ]
