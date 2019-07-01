from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'app.users'

    # noinspection PyUnresolvedReferences
    def ready(self):
        import app.users.signals  # noqa flake8
