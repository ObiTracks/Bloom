from django.apps import AppConfig


class mgmtAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mgmtApp'

    def ready(self):
        import mgmtApp.signals
