import os
try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve


def check_destination_path(path, name):
    """Check that path exists and is directory and that there is no file with
    name in that directory. Then returns full path to file.
    """
    file_path = os.path.join(path, name)
    if not os.path.isdir(path):
        raise IOError(
            '{} is not a directory or does not exist.'.format(path))
    if os.path.exists(file_path):
        raise IOError(
            '{} already exists in {}.'.format(name, path))
    return file_path
