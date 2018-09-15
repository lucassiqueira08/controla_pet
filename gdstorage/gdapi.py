from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import gdstorage.auth as auth

class GdApi:

    def __init__(self, scopes, client_secret_file, application_name):
        self.scopes = scopes
        self.client_secret_file = client_secret_file
        self.application_name = application_name
        self.auth_inst = auth.auth(self.scopes, self.client_secret_file, self.application_name)
        self.credentials = self.auth_inst.getCredentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.drive_service = discovery.build('drive', 'v3', http=self.http)

    def list_files(self, size):
        results = self.drive_service.files().list(
            pageSize=size, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))

    def upload_file(self, filename, filepath, mimetype):
        file_metadata = {'name': filename}
        media = MediaFileUpload(filepath,
                                mimetype=mimetype)
        file = self.drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def download_file(self, file_id, filepath):
        request = self.drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        with io.open(filepath, 'wb') as f:
            fh.seek(0)
            f.write(fh.read())

    def create_folder(self, name):
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service.files().create(body=file_metadata,
                                                 fields='id').execute()
        print('Folder ID: %s' % file.get('id'))

    def search_file(self, size, query):
        results = self.drive_service.files().list(pageSize=size,
                                                  fields="nextPageToken, files(id, name, kind, mimeType)",
                                                  q=query).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(item)
                print('{0} ({1})'.format(item['name'], item['id']))


gdapi = GdApi(scopes='https://www.googleapis.com/auth/drive',
              client_secret_file='../credentials.json',
              application_name='Drive API Python')
