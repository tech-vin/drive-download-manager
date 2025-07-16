import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
TOKEN_PATH = 'token.pickle'
CREDS_PATH = 'credentials.json'

def get_drive_services():
    """
    Performs OAuth 2.0 installed-app flow, caches credentials in token.pickle,
    and returns an authorized Google Drive API service object.
    """

    creds = None

    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token_file:
            creds = pickle.load(token_file)
    
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, 'wb') as token_file:
            pickle.dump(creds, token_file)

    service = build('drive', 'v3', credentials=creds)
    return service