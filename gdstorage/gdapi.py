from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

scopes = 'https://www.googleapis.com/auth/drive'
client_secret_file = '../credentials.json'
application_name = 'Drive API Python'


class GdApi:

    store = file.Storage('gdstorage/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scopes)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))

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

    def upload_file(self, filename, mimetype, filepath):
        file_metadata = {'name': filename}

        media = MediaFileUpload(filepath,
                                mimetype=mimetype)

        file = self.drive_service.files().create(body=file_metadata,
                                                 media_body=media,
                                                 fields='id').execute()
        return file.get('id')

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

    def search_folder_by_name(self, name):
        response = []
        results = self.drive_service.files().list(
            pageSize=1000, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        for item in items:
            if item['name'] == name:
                response.append(item)

        if not response:
            return []
        else:
            return response

    def create_folder(self, name):
        folder_exist = self.search_folder_by_name(name)

        if folder_exist == []:

            file_metadata = {
                'name': name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': 'Morumbichos'
            }

            folder = self.drive_service.files().create(body=file_metadata,
                                              fields='id').execute()
            return folder['id']
        else:
            return 'Diretório existente'

    def search_file_by_name(self, query, size=1000):
        results = self.drive_service.files().list(pageSize=size,
                                                  fields="nextPageToken, files(id, name)",
                                                  q="name contains '%s'" % query).execute()
        items = results.get('files', [])
        if not items:
            return []
        else:
            return items

    def get_file_by_id(self, file_id):
        file = self.drive_service.files().get(fileId=file_id).execute()

        if file == {}:
            return {}
        else:
            return file

    def get_src_image(self, file_id):
        file = self.get_file_by_id(file_id)
        url = "https://drive.google.com/uc" + "?id=" + file_id + "&export=download"
        return url
