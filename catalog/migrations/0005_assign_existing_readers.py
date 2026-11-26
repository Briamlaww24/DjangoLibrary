from django.conf import settings
from django.db import migrations


def assign_existing_readers(apps, schema_editor):
    database = schema_editor.connection.alias
    group, _ = apps.get_model("auth", "Group").objects.using(database).get_or_create(name="consultores")
    user_model = apps.get_model(settings.AUTH_USER_MODEL)
    users = user_model.objects.using(database).filter(is_superuser=False, groups__isnull=True)
    for user in users.iterator():
        user.groups.add(group)


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_library_entities"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [migrations.RunPython(assign_existing_readers, migrations.RunPython.noop)]
