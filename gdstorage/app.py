from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload
from django.http import HttpRequest
from gdstorage.auth import conection

service = conection()


def upload_images(name, path):
    file_metadata = {'name': name}
    media = MediaFileUpload(path, mimetype='image/jpeg')
    file = service.files().create(
                                body=file_metadata,
                                media_body=media,
                                fields='id').execute()

    print('[UPLOAD IMAGE] File ID: %s' % file.get('id'))
    return {'id': file.get('id')}


def upload_docs(name, path):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(path,
                            mimetype=('application/msword', 'application/pdf'),
                            resumable=True)

    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()

    print('[UPLOAD DOC] File ID: %s' % file.get('id'))
    return {'id': file.get('id')}


def search_file(size, query):
    results = service.files().list(pageSize=size,
                                   fields="nextPageToken, files(id, name, mimeType)",
                                   q=query).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
        return []
    else:
        search = []
        for item in items:
            print('[GET FILE] {0} ({1})'.format(item['name'], item['id']))
            search.append({'id': item.get('id')})
        return search
