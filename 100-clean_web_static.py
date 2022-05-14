#!/usr/bin/python3
"""
This module provides
    - Function to generate .tgz file
    - Function tha distribuites an archive to your servers
    - Function that deletes out-of-date archives

Functions
---------
    do_pack
    do_deploy
    do_clean
    deploy
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
    if exists(archive_path) is False:
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
        run("sudo rm -rf /data/web_static/current")
        # Create new symbolic link
        run("sudo ln -fs {} /data/web_static/current".format(directory))
        # ===== Return value =====
        return True
    except Exception:
        return False


def deploy():
    """
    Function definition that creates and distributes an archive to your
    web servers
    """
    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)


def do_clean(number=0):
    """
    Function definition that deletes out-of-date archives
    """
    number = int(number)

    if number not in [0, 1, 2]:
        return None

    if number == 0:
        number = 2
    else:
        number += 1

    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = '/data/web_static/releases'
    run(
        "cd {} ;sudo ls -t | sudo tail -n +{} | sudo xargs rm -rf"
        .format(path, number)
    )
