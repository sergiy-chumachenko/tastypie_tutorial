from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models import signals


class ServicesConfig(AppConfig):
    name = 'services'

    # This line dispatches signal to Tastypie to create APIKey
    def ready(self):
        from tastypie.models import create_api_key
        User = get_user_model()
        signals.post_save.connect(create_api_key, sender=User)
