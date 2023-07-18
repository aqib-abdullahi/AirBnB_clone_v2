#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    a = datetime.now()
    now = a.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
