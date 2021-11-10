#!/usr/bin/python3
import glob
import pyheif
  
# Returns a list of names in list files.
files = glob.glob('/home/priyank/Company/Shaip/image_scraping/image-utils/New_folder/**/*.*', 
                   recursive = True)
for file in files:
    if file.endswith('.HEIC'):
        try:
            heif_file = pyheif.read(file)
            print(file,",",heif_file.size)
        except:
            print(file)
            pass
    else:
        pass
