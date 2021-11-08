from __future__ import print_function
import pickle
import os
import io
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gdrive



def main():
    service = gdrive.get_drive()
    folder_id = '1OBWmmma1LTr2eGUHHhpa4aap7e-mO7ED'
    directory = "p1"
    parent_path = "/home/priyank/Company/Shaip/Drive-download"
    #gdrive.create_folder(directory,parent_path)
    #gdrive.get_file_list(service,folder_id)
    gdrive.download_gdrive_folder(service,folder_id,parent_path,directory)
    
    

if __name__ == '__main__':
    main()
