from django.conf import settings

# If  NEWS_TAGGING set to True, but tagging application does not installed,
# set NEWS_TAGGING to False

if 'tagging' in settings.INSTALLED_APPS:
    NEWS_TAGGING = getattr(settings, 'NEWS_TAGGING', True)
else:
    try:
        import tagging
        NEWS_TAGGING = getattr(settings, 'NEWS_TAGGING', False)
    except ImportError:
        NEWS_TAGGING = False
