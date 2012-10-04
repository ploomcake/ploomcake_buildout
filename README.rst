Ploomcake
=========
This is the buildout folder of Ploomcake, which extends the standard Plone buildout. 

What is Ploomcake
=================

Ploomcake is a distribution of the powerful open source Plone CMS (http://plone.org) that lets you create an out-of-the-box website or intranet.
It automatically includes in your portal a selection of the best third-party open source plugins: mobile support with responsive theme, easy forms generation support, tabs and slideshows goodies, multilanguage support, and much more.
Before you go on you should know that it is also available a pre packaged unified installer. Go and get it on the official web site (coming soon).
If you are an expert user (or a developer) you can go on following this guide.

How to install
==============

Prepare the Plone buildout
--------------------------
Install Plone 4.1.6 using Unified installer. You can get it on plone.org (http://plone.org/products/plone/releases/4.1.6).
After the installation rename the buildout.cfg of the Plone instance folder as "configuration.cfg". This step is very important because the Ploomcake buildout will extend this file.

Check out this folder
---------------------
This folder must be placed in the instance directory. Go to the instance directory and clone this repository from github using::

    git clone git@github.com:ploomcake/ploomcake_buildout.git config.d

Pick a buildout
---------------
In the config.d folder we have two main buildout files: start_develop.cfg and start_production.cfg
Choose the one to install according to what kind of installation you prefer. If you want to:

    * build a developer environment (with a lot of useful tools, test etc.), pick the start_develop.cfg
    * build a production environment, pick the start_production.cfg

Launch the buildout
-------------------
Copy the buildout file you picked in the parent folder (the instance directory), rename as buildout.cfg and launch::

    bin/buildout

Enjoy!!
-------
Ploomcake is installed correctly. You can give a try launching::

    bin/plonectl start

Ploomcake will respond to http://localhost:8080.


Extending this buildout (developers)
====================================
The cleanest way to extend this buildout is to create another folder like this in the buildout. We have prepared a precompiled folder called "extend_config.d".
In this folder you can customize and extend the buildout configuration. In particular this buildout inherits the project.cfg.
To use the new extended buildout you have to copy the start_devel.cfg or start_production.cfg in the instance directory and relaunch the buildout using one of these files.
You can rename the file you choose as buildout.cfg and relaunch bin/buildout

License
=======
This is free software (see license/LICENSE.txt,  license/LICENSE.GPL).
