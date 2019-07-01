#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
local.py is same as manage.py, but works only for local dev setup (without Docker, only virtualenv and sqlite).
So you should use 'python local.py migrate' for example.
Added this for better integration with Visual Studio Code, and fast local dev env setup.
It depends on local_venv.py, local settings file.
This settings are fully separated from docker and prod settings.
"""


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local_env')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
