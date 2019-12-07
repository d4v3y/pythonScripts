import os
import sys
import gzip
import shutil

backupDir = os.path.join(".backup")
currentDir = os.getcwd()

if not os.path.exists(backupDir) :
    os.mkdir(backupDir)

for item in os.listdir(currentDir) :

    source = os.path.join(currentDir, item)
    destination = os.path.join(backupDir, item)
    
    if os.path.isdir(source) :
        shutil.copytree(source, destination, symlinks=True, ignore=shutil.ignore_patterns('backup'))
    else :
        if not os.path.exists(destination) or os.stat(source).st_mtime - os.stat(destination).st_mtime > 1:
                shutil.copy2(source, destination)