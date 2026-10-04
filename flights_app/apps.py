from django.apps import AppConfig


class FlightsAppConfig(AppConfig):
    name = 'flights_app'
    
    def ready(self):
        import flights_app.signals  # Import signals to ensure they are registered
