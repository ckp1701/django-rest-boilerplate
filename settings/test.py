# Tests configuration file

from settings.common import *  # noqa flake8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa flake8
    }
}
