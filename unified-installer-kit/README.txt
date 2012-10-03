Transform an unified installer into a Ploomcake installer
=========================================================
This directory contains the software kit needed to transform a Plone unified
installer into a Ploomcake unified installer.


Step 0 Prerequisites:
---------------------

    - Download and unpack a Plone unified installer
    - Install Plone (install.sh standalone --target=/${plone folder})
    - Install Ploomcake following the instruction in ../README.txt
    - Delete and unpack again the Plone unified installer (eg. rm -rf Plone-4.1.3-UnifiedInstaller/ )
      This is because it is modified during the install process.
    - From now on I'll assume that the folder "/${plone folder}" is the folder where Plone is installed while 
      "/${installer folder}" is the freshly unpacked Unified installer folder. 


Step 1 Update the eggs:
-----------------------

    - go to /${plone folder}/zinstance/config.d/unified-installer-kit and
      run python update_packages.py /${plone folder}
      for example:
      python update_packages.py ../../../
    - this will create a packages/buildout-cache.tar.bz2
    - if the command returns something like: "Ooops: ['python_ldap-2.4.9']"
      this means that something gone wrong with this packages.
      We must add manually the packages in the buildout-cache.tar.bz2 file
      for example we have to add
      /${plone folder}/buildout-cache/download/dist/python-ldap-2.4.9.tar.gz
    - copy buildout-cache.tar.bz2 in the "packages" directory of the "/${installer folder}"

Step 2 Update the skeleton:
---------------------------

    - export the directory config.d in "/${installer folder}/base_skeleton" 
    - copy config.d/start_devel.cfg and config.d/start_production.cfg in 
      "/${installer folder}/base_skeleton"
    - rename start_production.cfg as buildout.cfg
    - export all the repositories under the "src" folder in 
      "/${installer folder}/base_skeleton/src"
    - comment out the row with "sources.cfg" in config.d/project.cfg

Step 3 Patch the installer:
---------------------------
    - copy create_instance.py in /${installer folder}/helper_scripts/create_instance.py.
     (The only customization is row 174: configuration.cfg instead of buildout.cfg)
    
Step 4 Pack the installer:
--------------------------
    - rename the unified installer dirs in Ploomcake-VERSION-UnifiedInstaller
    - launch: tar cvzf Ploomcake-VERSION-UnifiedInstaller.tar.gz  /installer/Ploomcake-VERSION-UnifiedInstaller


