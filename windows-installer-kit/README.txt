What is this
============
This is a procedure to build a Windows installer of Ploomcake.

Warning
-------
This procedure is a path across a minefield. Follow everything fastidiously in
the right order otherwise you'll find youself bogged down debugging !

Step 1: installer prerequisites
-------------------------------
- Install subversion for windows
- Install GIT for windows http://code.google.com/p/msysgit
- Install Microsoft Windows SDKs v7.1:
    (http://www.microsoft.com/en-us/download/details.aspx?id=8279)
- Install Inno setup 5 (http://www.jrsoftware.org/)

Be sure that these paths are added to your "path" environment var:

    C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin
    C:\Program Files\Subversion\bin
    C:\Program Files\Inno Setup 5
    C:\Program Files\git (this is automatic)

Step 2: Install Ploomcake manually
----------------------------------
- Install the plone windows installer (tested with version 4.1.6)
- Copy the config.d directory in c:\Plone41
- Copy start_windows.cfg in c:\Plone41
- rename buildout.cfg as configuration.cfg
- rename start_windows.cfg as buildout.cfg
- launch bin\buildout.exe
- comment out the row with "sources.cfg" in config.d/project.cfg

Step 3: installer setup
-----------------------
Substitute the folder c:\Plone41\docs with the docs on this directory.
Substitute installer.cfg with the file in this directory.
Copy ploomcake.html in the c:\Plone41 directory
Remove Ep7.html in c:\Plone41
check the version of distribute inside bin\buildout-script.py and fix the pin
inside configuration.cfg

Step 4: Build the installer
---------------------------
launch::

    bin\buildout.exe -c installer.cfg

and::

    bin\installer.exe

If everything is ok, after a while, the installer will be in c:\plone41\build.

Troubleshooting
----------------
If something goes wrong remove c:\Plone41\build and c:\Pcake13 before other attemps.
If something goes wrong with installer.exe put a pdb into src\enfold\recipe\innosetup (installer.py) and try:

    python\python bin\installer-script.py

References
----------
http://plone.org/documentation/kb/plone-4-windows-installer
http://package.enfoldsystems.com/docs/windows.html
