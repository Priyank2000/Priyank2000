from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='\nThis program Read JSON file... ')
parser.add_argument('file_name',help='Add JSON file name') 
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
print("-------------------**********-------------------")

text_file = open("danish.txt", "a")
n = text_file.write(soup.get_text())
text_file.close()