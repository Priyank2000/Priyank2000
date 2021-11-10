from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='\nThis program Read JSON file... ')
parser.add_argument('file_name',help='Add JSON file name') 
args = parser.parse_args()
name = args.file_name.split('-')[1]
image1 = Image.open(args.file_name)
im1 = image1.convert('RGB')
im1.save(name+'.pdf')