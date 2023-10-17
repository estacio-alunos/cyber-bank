from django.apps import AppConfig


class SetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'setup'

    def ready(self):
        # Makes sure all signal handlers are connected
        from setup import handlers  # noqa