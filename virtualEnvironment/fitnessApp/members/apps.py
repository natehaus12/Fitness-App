from django.apps import AppConfig
from django.core.signals import setting_changed


class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'

            # add this
    def ready(self):
            from . import signals
            import members.signals  # noqa

class UserConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'users'

        # add this
        def ready(self):
            from . import signals
            import users.signals  # noqa
