import json
import argparse

parser = argparse.ArgumentParser(description='\nThis program Read JSON file... ')
parser.add_argument('url_name',help='Add URL name')
args = parser.parse_args()

file = open('collinfo.json',"r")
json_data = json.load(file)
file.close()
#print(json.dumps(json_data, indent=4, sort_keys=True))
for i in json_data:
    #print(i['cdx-api']+"?url="+args.url_name+"&output=json")
    print(('{}?url=%2A.{}&output=json'.format(i['cdx-api'], args.url_name)).replace('http', 'https'))
    