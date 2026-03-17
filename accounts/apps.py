from django.apps import AppConfig


class AccountsConfig(AppConfig):
    deafult_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals
