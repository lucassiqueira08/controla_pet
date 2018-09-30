from __future__ import print_function

import io




from apiclient.http import MediaFileUpload, MediaIoBaseDownload
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

scopes = 'https://www.googleapis.com/auth/drive'
client_secret_file = 'credentials.json'
application_name = 'Drive API Python'


class GdApi:

    store = file.Storage('token.json')
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

    def upload_file(self, filename, mimetype, filepath, upload_mimeType):
        if mimetype == 'image/jpeg':
            folder_id = self.create_folder("Images")
        else:
            folder_id = self.create_folder("Documentos")

        file_metadata = {'name': str(filename),
                         'parents': folder_id,
                         'mimeType': upload_mimeType}

        media = MediaFileUpload(filepath,
                                mimetype=mimetype,
                                resumable=True)

        file = self.drive_service.files().create(body=file_metadata,
                                                 media_body=media,
                                                 fields='id, parents').execute()
        self.move_files_between_folders(file.get('id'), folder_id)

        return file.get('id')

    def move_files_between_folders(self, file_id, folder_id):
        # Retrieve the existing parents to remove
        file = self.drive_service.files().get(fileId=file_id,
                                              fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))

        # Move the file to the new folder
        file = self.drive_service.files().update(fileId=file_id,
                                                 addParents=folder_id,
                                                 removeParents=previous_parents,
                                                 fields='id, parents').execute()

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
            folder_id = '164t7EFFY3R4MKNmOsYt4TuOtroIgUfFr'
            file_metadata = {
                'name': name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': folder_id
            }

            folder = self.drive_service.files().create(body=file_metadata,
                                                       fields='id').execute()
            return folder['id']
        else:
            return folder_exist[0]['id']

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

    def get_src_file(self, file_id, mimetype):
        if mimetype == 'image/jpeg':
            url = "https://drive.google.com/uc" + "?id=" + file_id + "&export=download"
            return url

        elif mimetype == 'plan/text' or mimetype == 'application/pdf':
            url = "https://drive.google.com/uc" + "?id=" + file_id + "&export=download"
            return url

        elif mimetype == 'text/docx':
            url = 'https://docs.google.com/document/d/' + file_id + '/export?format=pdf'
            return url

        elif mimetype == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
            url = 'https://docs.google.com/presentation/d/' + file_id + '/export/pdf'
            return url

        elif mimetype == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            url = 'https://docs.google.com/spreadsheets/d/' + file_id + '/export?format=pdf'
            return url
        else:
            try:
                url = "https://drive.google.com/uc" + "?id=" + file_id + "&export=download"
                return url
            except Exception:
                return "Arquivo inexistente"

    def delete_file_by_id(self, file_id):
        self.drive_service.files().delete(fileId=file_id).execute()
