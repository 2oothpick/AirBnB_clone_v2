#!/usr/bin/python3
"""
Generate .tgz files
"""
from time import strftime
from fabric.api import local

def do_pack():
    """Generate a .tgz file of web_static folder"""
    try:
        # create versions folder
        local("mkdir -p versions")
        # compress to versions folder
        time = f"{strftime('%Y%m%d%H%M%S')}"
        local(f"tar -cvzf versions/web_static_{time}.tgz web_static/")
        # return filename
        return f'verizon/web_static_{time}.tgz'
    except:
        return None
