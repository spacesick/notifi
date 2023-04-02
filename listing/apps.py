from django.apps import AppConfig


class ListingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'listing'

    def ready(self):
        from . import signals