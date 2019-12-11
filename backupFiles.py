import os
import shutil

backupDir = ".backup"
currentDir = os.getcwd()

# Check if ".backup" folder is created
if not os.path.exists(backupDir) :
    os.mkdir(backupDir)

# Copy every file and directory in current directory to .backup
for item in os.listdir(currentDir) :

    source = os.path.join(currentDir, item)
    destination = os.path.join(backupDir, item)
    
    # Copy files/folders
    if os.path.isdir(source) :
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns(backupDir))
    else :
        if not os.path.exists(destination) or os.stat(source).st_mtime - os.stat(destination).st_mtime > 1:
                shutil.copy2(source, destination)