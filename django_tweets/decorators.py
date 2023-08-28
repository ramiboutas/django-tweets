from django.conf import settings

from .exceptions import SettingError


def check_settings(func):
    settings_to_check = (
        "TWITTER_BEARER_TOKEN",
        "TWITTER_API_KEY",
        "TWITTER_API_KEY_SECRET",
        "TWITTER_ACCESS_TOKEN",
        "TWITTER_ACCESS_TOKEN_SECRET",
    )

    def wrapper(*args, **kwargs):
        for setting in settings_to_check:
            if getattr(settings, setting, None) is None:
                raise SettingError("Please provide a setting value to %s" % setting)
        return func(*args, **kwargs)

    return wrapper
