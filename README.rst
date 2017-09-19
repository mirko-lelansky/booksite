##########
Booksite
##########

This project is a simple use case to demonstrate the integration
of different NoSql systems in python.

=================
Implementation
=================

---------------
Dependencies
---------------

To build and run the project you need python 3 with django.

---------------
Installation
---------------

To install this project run first :code:`pip -r requierements.txt`
. If you want to switch the cache backend to voldemort you need an installed
`Voldemort Cluster <http://www.project-voldemort.com/>`_.

-----------
Usage
-----------

First create a mysql user and a database. Then change the database url in the
settings.py file. After that you can run the migrations with
:code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py migrate`.
Then you must create a super user or admin user with :code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py createsuperuser`.
After that you can optionally import the database dumb with :code:`BOOKSITE_USER="{dbuser} BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py loaddata --database default dump.json`.
The last thing what you have to do is to start the server with :code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py runserver`.

You can delete the BOOKSITE_USER and BOOKSITE_PASSWORD prefix when you have the
corresponding environment variables are set.

In the server_config folder you find a example cluster configuration which
starts the REST-connector on port 8082. If you want to use this config find the
voldemort-server script in the voldemort bin folder and start the following
command :code:`voldemort-server.{sh|bat} ./server_config/test_cluster`. Then you
can starts the server with :code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py runserver --configuration=Voldemort`
to switch the backend to voldemort.

==============
Contributing
==============

========
License
========

The project is licensed under the Apache 2 License -
see the LICENSE.rst file for details.
