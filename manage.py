#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys
from dotenv import load_dotenv


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
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
    project_folder = os.path.expanduser('base')
    load_dotenv(os.path.join(project_folder, '.env'))

    if 'test' in sys.argv:
        os.environ.setdefault('TESTING', 'True')
        if '--no-logs' in sys.argv:
            print('> Disabling logging levels of ERROR and below.')
            sys.argv.remove('--no-logs')
            logging.disable(logging.ERROR)

    main()
