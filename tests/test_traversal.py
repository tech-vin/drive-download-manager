# test_traversal.py

from downloader.auth import get_drive_services
from downloader.traversal import traverse_folder

if __name__ == '__main__':
    drive = get_drive_services()
    folder_id = input("Enter Google Drive folder ID: ").strip()
    print(f"\nContents of folder {folder_id}:\n")
    for meta, rel in traverse_folder(drive, folder_id):
        print(f"{rel:60}  ({meta['id']})")
