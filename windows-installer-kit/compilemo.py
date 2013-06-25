import os
import os.path
import sys

#msgfmt = "'C:\\Program Files (x86)\\Poedit\\bin\\
msgfmt = "msgfmt.exe"

def compilemo(p):
    messages = os.path.join(p, 'LC_MESSAGES')
    if not os.path.isdir(messages):
        return
    for fname in os.listdir(messages):
        fin = os.path.join(messages, fname)
        if os.path.isfile(fin) and fin.endswith('.po'):
            fout = os.path.splitext(fin)[0] + '.mo'
            os.system('%s -o "%s" %s' % (msgfmt, fout, fin))

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    IndexError:
        print """Utility to compile .po into .mo. 
Use only for Windows ! For others OS it's much easier to install gettext and start Plone.
Before use this install msgfmt.exe (poedit should include this utility) and set the path environment variable accordingly.

Use: compilemo.py rootpath

Example: compilemo.py eggs
"""



    for root, dirs, files in os.walk(os.path.abspath(path)):
        if root.endswith('locales'):
            print "Compiling %s" % root
            for d in dirs:
                fullpath = os.path.join(root, d)
                compilemo(fullpath)
        

