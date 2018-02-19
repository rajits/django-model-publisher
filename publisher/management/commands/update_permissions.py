from django.apps import apps
from django.core.management.base import BaseCommand
from django.contrib.auth.management import create_permissions


class Command(BaseCommand):
    args = '<app app ...>'
    help = 'reloads permissions for specified apps, or all apps if no args are specified'

    def handle(self, *args, **options):
        models = apps.get_models()
        if not args:
            app_labels = [model._meta.app_label for model in models]
        else:
            app_labels = [arg for arg in args]
        for app_label in app_labels:
            try:
                app_config = apps.get_app_config(app_label)
            except LookupError:
                continue
            verbosity = int(options.get('verbosity', 0))
            create_permissions(app_config, models, verbosity)
