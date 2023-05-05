import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
import psycopg2


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']


def open_db_connection():
	# Creating postgres connection here
	conn = psycopg2.connect(
		host="localhost",
		database="Gmailapi",
		user="postgres",
		password="Brindha"
	 )
	return conn


def authenticate_service():
	"""Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
	creds = None
		# The file token.json stores the user's access and refresh tokens, and is
		# created automatically when the authorization flow completes for the first time.
	if os.path.exists('token.json'):
			creds = Credentials.from_authorized_user_file('token.json', SCOPES)
		# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
			# Save the credentials for the next run
		with open('token.json', 'w') as token:
			token.write(creds.to_json())
	try:
		# Connecting Gmail API
		service = build('gmail', 'v1', credentials=creds)
		return service

	except HttpError as error:
			print(f'An error occurred: {error}')