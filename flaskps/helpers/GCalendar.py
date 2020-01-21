from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']
def createEventCiclo(fIni,fFin):
	"""Shows basic usage of the Google Calendar API.
	Prints the start and name of the next 10 events on the user's calendar.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'flaskps/helpers/credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)

	# Call the Calendar API
	#print(datetime.datetime.now())
	#now = datetime.datetime.utcnow().isoformat()  + 'Z' # 'Z' indicates UTC time
	now = datetime.datetime.now().isoformat()  + 'Z' # 'Z' indicates UTC time
	#print(now)
	#now = now.
	#print('Getting the upcoming 10 events')
	#events_result = service.events().list(calendarId='b7lirf0e02eikfq3gtn3bctjn4@group.calendar.google.com', timeMin=now,
	#									maxResults=30, singleEvents=True,
	#									orderBy='startTime').execute()
	#events = events_result.get('items', [])

	#if not events:
	#	print('No upcoming events found.')
	#for event in events:
	#	start = event['start'].get('dateTime', event['start'].get('date'))
	#	print(start, event['summary'])

	EVENT = {
		'summary': 'Ciclo Lectivo: '+fIni+' A '+fFin,
		'start': {'dateTime': fIni+'T07:00:00-03:00'},
		'end':{'dateTime': fFin+'T23:00:00-03:00'}
	}
	
	eventRE = {
	  'summary': 'Appointment',
	  'location': 'Somewhere',
	  'start': {
		'dateTime': '2019-06-03T10:00:00.000-03:00',
		'timeZone': 'America/Argentina/Buenos_Aires'
	  },
	  'end': {
		'dateTime': '2019-06-03T10:25:00.000-03:00',
		'timeZone': 'America/Argentina/Buenos_Aires'
	  },
	  'recurrence': [
		'RRULE:FREQ=WEEKLY;UNTIL=20190701T170000Z',
	  ]
	}
	
	e = service.events().insert(calendarId='b7lirf0e02eikfq3gtn3bctjn4@group.calendar.google.com',
	   sendNotifications=False, body=EVENT).execute()
	   #sendNotifications=False, body=eventRE).execute()
	#print(e)
	#print 'Event created: %s' % (e.get('htmlLink'))
def createEventTaller(nomTaller,nucleo,fIni,fFin,hsIni,hsFin):
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'flaskps/helpers/credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)

	# Call the Calendar API
	#print(datetime.datetime.now())
	#now = datetime.datetime.utcnow().isoformat()  + 'Z' # 'Z' indicates UTC time
	now = datetime.datetime.now().isoformat()  + 'Z' # 'Z' indicates UTC time
	#fechaSplit = fIni.split()
	#print(fIni)
	feRec = fFin.split("-")
	eventRE = {
	  'summary': nomTaller,
	  'location': nucleo,
	  'start': {
		'dateTime': fIni+'T'+hsIni+':00.000-03:00',
		'timeZone': 'America/Argentina/Buenos_Aires'
	  },
	  'end': {
		'dateTime': fIni+'T'+hsFin+':00.000-03:00',
		'timeZone': 'America/Argentina/Buenos_Aires'
	  },
	  'recurrence': [
		'RRULE:FREQ=WEEKLY;UNTIL='+feRec[0]+feRec[1]+feRec[2]+'T170000Z',
	  ]
	}
	
	e = service.events().insert(calendarId='b7lirf0e02eikfq3gtn3bctjn4@group.calendar.google.com',
	   #sendNotifications=False, body=EVENT).execute()
	   sendNotifications=False, body=eventRE).execute()
	#print(e)
	#print 'Event created: %s' % (e.get('htmlLink'))	
