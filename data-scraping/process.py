import json
import sys
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import zlib
from io import BytesIO
from warcio.archiveiterator import ArchiveIterator
from bs4 import BeautifulSoup
from lib import utils
import string
import random
import os
from os import path

data = json.load(sys.stdin)
#print(json.dumps(data, indent = 2))
filename = data['filename']
offset = data['offset']
length = data['length']
status = data['status']
# print(status)
digest = data['digest']
filename = str(data['filename'])
last_byte = int(offset) + int(length)
byte_range = 'bytes='+str(offset)+'-'+str(last_byte) 

bucket = "commoncrawl"
client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
response = client.get_object(

    Bucket = bucket,
    Key = filename,
    Range = byte_range 
)
r = response['Body'].read(amt=None)
#print("\nDecompressed:\n")
decompressed = zlib.decompress(r,47)
# print(decompressed.decode())
file = BytesIO(decompressed)
fname = filename.replace('/','-')+'-'+offset
htmlname = path.exists('/home/priyank/Company/Shaip/scraping-data/htmls'+fname+'.html')
print(status)

if htmlname == False:
    if status == '200':
    
        for record in ArchiveIterator(file):
            html = record.content_stream().read()    
        print("--------------------------------------------------------------")
        soup = BeautifulSoup(html,'html5lib')
        datas = soup.prettify()
        letters = string.ascii_lowercase
        filePathname = os.path.join('htmls', fname + '.html')
        with open(filePathname, 'w') as fp:
            fp.write(str(datas))
            file.close()
