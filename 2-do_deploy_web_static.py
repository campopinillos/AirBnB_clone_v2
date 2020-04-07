#!/usr/bin/python3
"""Script that distributes an archive to your web servers"""
from fabric.api import run, put, env
from datetime import datetime
from os import path


env.hosts = ['104.196.15.117', '52.200.30.119'] 
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploy"""
    if not path.exists(archive_path):
        return False

