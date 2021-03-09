from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'

    def ready(self):
        from pages.scheduler import scheduler
        scheduler.start()
