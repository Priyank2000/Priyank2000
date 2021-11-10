import fitz # PyMuPDF
from PIL import Image
import os

def getPhysicalSize(fn):

    #Open the image file and get the size in pixels
    im = Image.open(fn)
    width, height = im.size
    dpi = im.info['dpi']
    return dpi


path = "/home/priyank/Company/Shaip/image_scraping/pdfimages/data"
os.chdir(path)

for fn in (fns for fns in os.listdir('.') if fns.lower().endswith(('.jpg', '.jpeg'))):
    h_dpi,v_dpi = getPhysicalSize(fn)
    print(fn,",",h_dpi,":",v_dpi)
