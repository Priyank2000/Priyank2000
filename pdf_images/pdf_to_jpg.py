from pdf2image import convert_from_path
import argparse

parser = argparse.ArgumentParser(description='\nThis program Read JSON file... ')
parser.add_argument('file_name',help='Add JSON file name') 
parser.add_argument('dpi',help='select dpi')
args = parser.parse_args()

fname = args.file_name.replace(".pdf", "")
pages = convert_from_path(args.file_name)
for idx,page in enumerate(pages):
	page.save('pdf-'+fname+'-page'+str(idx)+'.jpg', dpi=(int(args.dpi),int(args.dpi)))
	
# To run put script near pdf file
# python3 pdf_to_jpg.py "file name" dpi-number
# eg: dpi-number = 200
