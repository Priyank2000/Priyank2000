from videoprops import get_video_properties
import glob
from argparse import ArgumentParser
import pandas as pd

parser = ArgumentParser()
parser.add_argument('-i', '--input', required=True)
args = parser.parse_args()

files = glob.glob(args.input + '/**/*.*', 
                   recursive = True)
filelist = []
resolutionlist = []
for file in files:
    props = get_video_properties(file)
    resolution = str(props['width'])+'×'+str(props['height'])
    filelist.append(file)
    resolutionlist.append(resolution)
    print(filelist,resolutionlist)
    d = {'File Path' : filelist, 'Resolution': resolutionlist}
    df = pd.DataFrame(data=d)
    df.to_csv('output.csv',index=False)     
