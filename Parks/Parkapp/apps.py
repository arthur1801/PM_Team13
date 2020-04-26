from django.apps import AppConfig


class ParkappConfig(AppConfig):
    name = 'Parkapp'

    def ready(self):
        import Parkapp.signals
