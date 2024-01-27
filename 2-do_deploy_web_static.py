#!/usr/bin/python3
"""
Generate .tgz files and deploys it to 
web servers
"""

from time import strftime
from fabric.api import *
import os

env.hosts = ['100.25.162.172', '54.152.165.14']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        # upload file to /tmp/
        put(archive_path, "/tmp/")
        # create target directory
        run("sudo mkdir -p {}".format(newest_version))
        # uncompress folders to target_directory
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        # delete archive
        run("sudo rm {}".format(archived_file))
        # move files from web_static to root of target folder
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        # delete empty web_static directory
        run("sudo rm -rf {}/web_static".format(newest_version))
        # delete sym link /data/web_static/current
        run("sudo rm -rf /data/web_static/current")
        # create new sym link between /data/web_static/releases/arch and /data/web_static/current
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
