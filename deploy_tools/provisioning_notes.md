Provisioning a new site
======================

## Required packages:

* nginx
* python 3
* Git
* Pip
* virtualenv

e.g. on ubuntu

sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv

## Nginx virtual host config

* see nginx.template.conf
* replace SITENAME with, eg staging.my-domain.com

## upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with eg staging.my-domain.com

## Folder structure
Asumes we have a user account at /home/username

/home/username
|-sites
        |-SITENAME
            |-database
            |-source
            |-static
            |-virtualenv

