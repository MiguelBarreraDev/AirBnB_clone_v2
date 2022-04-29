#!/usr/bin/python3
"""
This module provides a function to generate .tgz file

Functions
---------
    do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Function definition that generates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        dest = "versions/web_static_{}.tgz".format(date)
        local("tar -cvf {} web_static".format(dest))
        return dest
    except Exception:
        return None
