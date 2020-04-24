# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# built-in package
import os
import sys
import random
import string
import tempfile
import shutil 

from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import uses_relative, uses_netloc, uses_params

_VALID_URLS = set(uses_relative + uses_netloc + uses_params)


def python_major_version() -> int:
    """Python Major Version"""
    return sys.version_info.major

def is_valid_url(url: str) -> bool:
    """Check to see if a URL has a valid protocol.

    Parameters
    ----------
    url: str or unicode

    Returns
    -------
    is_valid_url: bool
        If url has a valid protocol return True otherwise False.

    """

    try:
        return urlparse(url).scheme in _VALID_URLS
    except Exception:
        return False


def random_string(length:int) -> str:
    """Generate Random String

    Parameter
    ---------
    length: int
        Length of random string
    
    Return
    ------
    random_val: str
        Random alpha-numeric string
    """

    random_val = ""
    while length:
        random_val += random.choice(
            string.digits + string.ascii_lowercase + string.ascii_uppercase
        )
        length -= 1
    return random_val

def remove_file(filepath: str) -> bool:
    
    try:
        os.remove(filepath)
        return True
    except FileNotFoundError:
        return False

def get_file_name(file_path: str) -> str:
    """
    Return base file name.
    """
    
    return os.path.basename(file_path)

def get_file_name_without_extension(file_path: str) -> str:
    """
    Return base file name without extension.
    """
    
    file_name = os.path.basename(file_path)
    return '.'.join(file_name.split('.')[:-1])

def download_url(url: str) -> str:
    """Download file from specified url

    Parameter
    ---------
    url: str or unicode

    Return
    ------
    filepath: str or unicode
        Temporary filepath.
    """

    filename = "{}.pdf".format(get_file_name_without_extension(url))
    with tempfile.NamedTemporaryFile('wb', delete=False) as file:
        obj = urlopen(url)
        content_type = obj.info().get_content_type()
        if content_type != "application/pdf":
            raise NotImplementedError("File format not supported")
        file.write(obj.read())

    filepath = os.path.join(os.path.dirname(file.name), filename)
    shutil.move(file.name, filepath)

    return filepath





if __name__ == "__main__":
    print(get_file_name_without_extension("../../abc/ppp.pdf"))
    print(python_major_version())
    print(is_valid_url("https://d1.awsstatic.com/whitepapers/migrating-magento-to-aws.pdf"))
    filepath = download_url("https://d1.awsstatic.com/whitepapers/migrating-magento-to-aws.pdf")
    print(filepath)
    remove_file(filepath)