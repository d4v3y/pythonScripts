import os
import glob

for item in glob.glob('*.cxx') :

    fileName, fileExtension = os.path.splitext(item)
    os.rename(item, fileName + ".cpp")