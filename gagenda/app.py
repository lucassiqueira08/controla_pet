# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
client_secret_file = 'gagenda/credentials.json'

class GCalGoogle():
    store = file.Storage('gagenda/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    def criar(self , event):
        event = self.service.events().insert(calendarId='primary', body=event).execute()
           # print ('Event created: %s' % (event.get('id')))
        return event.get('id')   

    def deletar(self, id):
        self.service.events().delete(calendarId='primary', eventId=id).execute()

    def atualizar(self,id,sumary,start,end):
        event = service.events().get(calendarId='primary', eventId=id).execute()
        event['summary'] = sumary
        event['start']['dateTime'] = start #'2018-10-08T13:00:00-03:00'
        event['end']['dateTime'] = end #'2018-10-09T14:10:00-03:00'
        self.service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()





