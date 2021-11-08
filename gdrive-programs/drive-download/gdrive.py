from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.[t=]
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service

def create_textfile(f_id,f_name,service,parent_dir):
    file_id = f_id
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
        fh.seek(0)
        with open(os.path.join(parent_dir,f_name),'wb') as f:
            f.write(fh.read())
            f.close()

def create_folder(folder_name,parent_path):
    dir = folder_name
    print(dir)
    parent_dir = parent_path
    path = os.path.join(parent_dir, dir)
    parent_path = path
    os.mkdir(path) 
    return path

def get_file_list(service, folder_id):
    query = f"parents='{folder_id}'"
    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name,mimeType)",q=query).execute()
    items = results.get('files', [])
    print(items)
    return items

def download_folder(service, folder_id, parent_path):

    items = get_file_list(service,folder_id)
    print(items)
    for item in items:
        print('{0} ({1}) ({2})'.format(item['name'], item['id'],item['mimeType']))

        if item['mimeType'] == 'text/plain' or item['mimeType'] == 'video/mp4':
            parent_dir=parent_path
            create_textfile(item['id'],item['name'],service,parent_dir)
            print("Download text file",item['id'],item['name'],parent_dir)
        else:
            parent_path = create_folder(item['name'],parent_path)

            print("Create a folder",item['name'],os.path.join(parent_path,item['name']))
            os.mkdir(os.path.join(parent_path,item['name']))
            download_folder(service,item['id'],os.path.join(parent_path,item['name']))

# download_folder (service, folder_id, base_path, folder_name);
#    1. Create the folder with base_path/folder_name
#    2. Get List of Items
#    3. Iterate On Items Build Accordingly
#        If Item is text
#            Download the Text
#        else:
#            download_folder(service, item['id'], os.path.join(base_path, folder_name), item['name'])

# handlers = {
#    'text/plain': lambda service, item, base_path: create_textfile(item['id'], item['name'], service, base_path),
#    'application/vnd.google-apps.folder': lambda service, item, base_path: download_gdrive_folder(service, item['id'], base_path, item['name']),
#    'application/vnd.google-apps.document': lambda s,i,b: print("Unknown mimeType",i)
# }

def download_gdrive_folder(service, folder_id, base_path, folder_name):
    folder_path = os.path.join(base_path, folder_name)
    os.mkdir(folder_path)
    Items = get_file_list(service, folder_id)
    for item in Items:
        if item['mimeType'] == 'text/plain' or item['mimeType'] == 'image/jpeg' or item['mimeType'] == 'video/mp4' :
            create_textfile(item['id'],item['name'],service, folder_path)
        elif item['mimeType'] == 'application/vnd.google-apps.folder':
            download_gdrive_folder(service, item['id'], folder_path, item['name'])
        else:
            print("Unknown mimeType",item)
        # handlers[item['mimeType']](service, item, folder_path)



