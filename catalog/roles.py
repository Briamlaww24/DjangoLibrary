from django.contrib.auth.models import Group, Permission

ADMINISTRATORS = "administradores"
CONSULTANTS = "consultores"


def isCatalogAdmin(user):
    return user.is_superuser or user.groups.filter(name=ADMINISTRATORS).exists()


def configureRoles(using="default"):
    permissions = Permission.objects.using(using).filter(content_type__app_label="catalog")
    administrators, _ = Group.objects.using(using).get_or_create(name=ADMINISTRATORS)
    consultants, _ = Group.objects.using(using).get_or_create(name=CONSULTANTS)
    administrators.permissions.set(permissions)
    consultants.permissions.set(permissions.filter(codename__in=[
        "view_author", "view_book", "view_category", "add_book", "change_book", "delete_book",
    ]))
    return administrators, consultants
