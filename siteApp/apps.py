from django.apps import AppConfig


class siteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteApp'

    def ready(self):
        import siteApp.signals
        import accountsApp.signals