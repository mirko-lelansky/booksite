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
.

-----------
Usage
-----------

First create a mysql user and a database. Then change the database url in the
settings.py file. After that you can run the migrations with
:code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py migrate`.
Then you must create a super user or admin user with :code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py createsuperuser`.
After that you can optionally import the database dumb.
The last thing what you have to do is to start the server with :code:`BOOKSITE_USER="{dbuser}" BOOKSITE_PASSWORD="{dbpassword}" python ./manage.py runserver`.

You can delete the BOOKSITE_USER and BOOKSITE_PASSWORD prefix when you have the
corresponding environment variables are set.

==============
Contributing
==============

========
License
========

The project is licensed under the Apache 2 License -
see the LICENSE.rst file for details.
