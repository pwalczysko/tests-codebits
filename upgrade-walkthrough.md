Backup - priority
=================

First, back up your DB and OMERO directory as instructed by Jean-Marie in previous email (you can also read
https://omero.readthedocs.io/en/stable/sysadmins/server-upgrade.html
https://omero.readthedocs.io/en/stable/sysadmins/server-upgrade.html#perform-a-database-backup).

Check your docker container names
=================================

```
docker ps

# check the nanes of your containers in the docker ps output

CONTAINER ID   IMAGE                                   COMMAND                  CREATED         STATUS                 PORTS                              NAMES
4e31d2589f4c   openmicroscopy/omero-server:5           "/usr/local/bin/entr…"   2 weeks ago     Up 2 weeks             0.0.0.0:4063-4064->4063-4064/tcp   omero-setup-omeroserver-1
```

Check your present OMERO.server version
=======================================

```
docker exec -it omero-setup-omeroserver-1 bash

/opt/omero/server/OMERO.server/bin/omero admin diagnostics
# The output of this cmd will be showing an outdated version of OMERO.server, yours will be even lower. Latest is 5.6.17 - check https://www.openmicroscopy.org/omero/downloads/ 

...
Component:  OMERO.server                   5.6.16-ice36
...
# jump out of the container with Ctrl+D
```

Upgrade your server
===================

```
docker pull openmicroscopy/omero-server:5
....
Status: Downloaded newer image for openmicroscopy/omero-server:5
docker.io/openmicroscopy/omero-server:5
docker compose down
docker compose up -d

docker exec -it omero-setup-omeroserver-1 bash

/opt/omero/server/OMERO.server/bin/omero admin diagnostics
...
Component:  OMERO.server                   5.6.17-ice36
...

# jump out of the container with Ctrl+D
```

Check your OMERO.web version
============================

```
docker exec -it omero-setup-omeroweb-1 bash

source /opt/omero/web/venv3/bin/activate

(venv-3.12) bash-5.1$ pip freeze | grep web
omero-web==5.29.3

Ctrl+D to jump out of the docker container
```

Upgrade your OMERO.web and your OMERO.figure
============================================

```
docker pull openmicroscopy/omero-web-standalone:5
docker compose down
docker compose up  #note there is no -d so that you can cancel the process with Ctrl+C later

# Open a new terminal window

docker exec -it -u root omero-setup-omeroweb-1 bash

((venv-3.12) ) bash-5.1$ pip freeze | grep figure
omero-figure==7.3.1

((venv-3.12) ) bash-5.1$ pip install omero-figure==7.4.1
...

# Go back to the first terminal and cancel the process with Ctrl+C

docker container ls --all
# from the output, copy the CONTAINER ID of the container whose IMAGE is openmicroscopy/omero-web-standalone:5

docker commit <CONTAINER-ID-you-just-copied>

docker image ls
# from the output copy the IMAGE ID of the image which was created latest, it will have TAG <none>

docker tag <IMAGE-ID-you-just-copied> openmicroscopy/omero-web-standalone:5
docker image ls # the output should looks similar to below
REPOSITORY                                             TAG                         IMAGE ID       CREATED         SIZE
openmicroscopy/omero-web-standalone                    5                           d406e31bc3cb   4 minutes ago   1.18GB
...

docker compose up -d # this time you use -d

# login to OMERO.web as administrator and click on Figure -> once in Figure, check that Help > About gives you Figure 7.4.1. In top-right corner, you will see a red warning. Click on it and follow the instructions to download matchine Figure_to_pdf.py script. The red warning should vanish after that.



