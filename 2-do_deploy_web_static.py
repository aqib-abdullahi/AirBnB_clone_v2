#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os.path import exists

env.hosts = ['52.23.212.186', '3.89.155.70']

def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    a = datetime.now()
    now = a.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        filename_no_ext = filename.split(".")[0]
        put(archive_path, "/tmp/{}".format(filename))
        run("mkdir -p /data/web_static/releases/{}/".format(filename_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, filename_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(filename_no_ext, filename_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
