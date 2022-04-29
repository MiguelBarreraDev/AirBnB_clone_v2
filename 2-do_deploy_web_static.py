#!/usr/bin/python3
"""
This module provides
    - Function to generate .tgz file
    - Distribuites an archive to your servers

Functions
---------
    do_pack
"""
from os.path import exists
from datetime import datetime
from fabric.api import local, env, run, put

web_servers = {
    "server1": "34.148.228.218",
    "server2": "52.73.137.46"
}
env.hosts = list(web_servers.values())


def do_pack():
    """
    Function definition that generates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        dest = "versions/web_static_{}.tgz".format(date)
        local("tar -zcvf {} web_static".format(dest))
        return dest
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Function definition that distributes an archive to your web servers
    """
    if exists(archive_path) if False:
        return False

    try:
        # ===== Setup =====
        filename = archive_path.split("/")[-1]
        file_without_ext = filename.split(".")[0]
        path = "/data/web_static/releases/"
        directory = "{}{}".format(path, file_without_ext)
        # ===== Commands =====
        put(archive_path, "/tmp")
        # Create directory if don't exists
        run("sudo mkdir -p {}".format(directory))
        # Uncompress
        run("sudo tar -zxf /tmp/{} -C {}/".format(filename, directory))
        # Remove file of the web server and move others files
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv {}/web_static/* {}".format(directory, directory))
        run("sudo rm -rf {}/web_static".format(directory))
        # Create new symbolic link
        run("sudo ln -fs {} /data/web_static/current".format(directory))
        # ===== Return value =====
        return True
    except Exception:
        return False
