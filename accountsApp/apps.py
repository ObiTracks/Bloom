from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountsApp'

    def ready(self):
        import accountsApp.signals
        import siteApp.signals