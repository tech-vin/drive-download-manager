#from downloader.auth import get_drive_services
from downloader.auth import get_drive_services
if __name__ == '__main__':
    drive = get_drive_services()
    results = drive.files().list(pageSize=5, fields='files(id, name)').execute()
    items = results.get('files', [])
    for f in items:
        print(f"{f['name']} ({f['id']})")


#https://console.cloud.google.com/apis/credentials/consent?project=YOUR_PROJECT_ID
