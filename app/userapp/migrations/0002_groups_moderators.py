from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import migrations
from django.db.models import Q

from mainapp.models import Comment, Post


def add_group_permissions(apps, schema_editor):
    post_ct = ContentType.objects.get_for_model(Post)
    comment_ct = ContentType.objects.get_for_model(Comment)

    permission = Permission.objects.filter(
        Q(content_type=post_ct)
        |Q(content_type=comment_ct)
    )

    group, created = Group.objects.get_or_create(name="moderator")
    group.permissions.set(permission)


class Migration(migrations.Migration):
    dependencies = [
        ('userapp', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_group_permissions),
    ]
