#!/usr/bin/python3
"""
Generate .tgz files and deploys it to
web servers
"""

from time import strftime
from fabric.api import env, run, put
import os

env.hosts = ['100.25.162.172', '54.152.165.14']
env.user = "ubuntu"


def do_pack():
    """
    generates .tgz archive folder
    """
    try:
        local("mkdir -p versions")
        timefrmat = strftime("%Y%M%d%H%M%S")
        filenme = "versions/web_static_{}.tgz".format(timefrmat)
        local("tar -cvzf {} web_static/".format(filenme))
        return filenme
    except Exception:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filenme = archive_path.split("/")[-1]
        nme = filenme.split(".")[0]
        path_r = "/data/web_static/releases/{}/".format(nme)
        path_c = "/data/web_static/current"
        put(archive_path, "/tmp/{}".format(filenme))
        """put(archive_path, "/tmp/")"""
        run("mkdir -p {}".format(path_r))
        run("tar -xzf /tmp/{} -C {}".format(filenme, path_r))
        run("rm /tmp/{}".format(filenme))
        run("mv {}web_static/* {}".format(path_r, path_r))
        run("rm -rf {}web_static".format(path_r))
        run("rm -rf {}".format(path_c))
        run("ln -s {} {}".format(path_r, path_c))
        print('New version deployed!')
        return True
    except Exception:
        return False
