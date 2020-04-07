#!/usr/bin/python3
"""Script that generates a .tgz archive"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Tar archive"""
    try:
        filename = "versions/web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except:
        return None
