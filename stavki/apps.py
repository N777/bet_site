from django.apps import AppConfig


class StavkiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stavki'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import stavki.signals