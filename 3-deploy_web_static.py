#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os.path import exists

env.hosts = ['52.23.212.186', '3.89.155.70']
env.user = ['ubuntu']
env.key_filename = {
    '52.23.212.186': '~/.ssh/id_rsa',
    '3.89.155.70': '~/.ssh/server2'
}

def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    a = datetime.now()
    now = a.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))

def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not exists(archive_path):
        return False

    try:
         # Get the current host being executed
        current_host = env.host_string

        # Set the private key for the current host
        env.key_filename = env.key_filename.get(current_host)

        filename = archive_path.split("/")[-1]
        filename_no_ext = filename.split(".")[0]
        put(archive_path, "/tmp/{}".format(filename))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(filename_no_ext))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, filename_no_ext))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(filename_no_ext, filename_no_ext))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(filename_no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False

def deploy():
    """Creates and Distributes a .tgz archive through web servers
    """

    archive = do_pack()
    if not archive:
        return False

    return do_deploy(archive)
