from django.apps import AppConfig


class FundingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fundings'
    verbose_name = 'Donateurs'  # Définit le nom affiché dans l'admin
