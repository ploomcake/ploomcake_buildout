Step 1: Install Ploomcake manually
----------------------------------
- Install the plone windows installer (tested with version 4.1.6)
- Copy the config.d directory in c:\Plone41
- Copy start_windows.cfg in c:\Plone41
- rename buildout.cfg as configuration.cfg
- rename start_windows.cfg as buildout.cfg
- comment out the row with "sources.cfg" in config.d/project.cfg
- launch bin\buildout.exe

Step 2: installer prerequisites
-------------------------------
- Install subversion for windows
- Install Microsoft Windows SDKs v7.1:
    (http://www.microsoft.com/en-us/download/details.aspx?id=8279)
- Install Inno setup 5 (http://www.jrsoftware.org/)


Add this paths to the paths environment var:

    C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin
    C:\Program Files\Subversion\bin
    C:\Program Files\Inno Setup 5


Step 3: installer setup
-----------------------
Substitute the folder c:\Plone41\docs with the docs on this directory.
Substitute installer.cfg with the file in this directory.
Copy ploomcake.html in the c:\Plone41 directory
Remove Ep7.html in c:\Plone41
Remove the version pin of distribute in buildout.cfg


Step 4: Build the installer
---------------------------
launch bin\buildout.exe -c installer.cfg
If everything is ok, after a while, the installer will be in c:\plone41\build.

Troubleshooting
----------------
If something goes wrong remove c:\Plone41\build and c:\Pcake before other attemps.

References
----------
http://plone.org/documentation/kb/plone-4-windows-installer
http://package.enfoldsystems.com/docs/windows.html
