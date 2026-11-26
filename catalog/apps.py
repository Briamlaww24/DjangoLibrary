from django.apps import AppConfig
from django.db.models.signals import post_migrate


def createCatalogRoles(sender, using, **kwargs):
    from django.contrib.auth.management import create_permissions

    from catalog.roles import configureRoles

    create_permissions(sender, using=using, apps=kwargs["apps"], verbosity=0)
    configureRoles(using)


class CatalogConfig(AppConfig):
    name = "catalog"

    def ready(self):
        post_migrate.connect(createCatalogRoles, sender=self)
