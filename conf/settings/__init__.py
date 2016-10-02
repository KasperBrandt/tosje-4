from os.path import abspath, dirname, join, exists
from warnings import warn

try:
    from .site_settings import *  # noqa
except ImportError:
    path = dirname(abspath(__file__))
    file_path = join(path, 'site_settings.py')
    if not exists(file_path):
        message = 'You need to create %s' % file_path
        warn(message)
        from .defaults import *  # noqa
    else:
        raise
