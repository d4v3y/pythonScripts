import os
import glob

# Retrieve .cxx fiiles from current directory
for item in glob.glob('*.cxx') :

    # Split file name and rename files
    fileName, fileExtension = os.path.splitext(item)
    os.rename(item, fileName + ".cpp")
