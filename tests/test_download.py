# test_download.py

from downloader.auth import get_drive_services
from downloader.traversal import traverse_folder
from downloader.download import download_file

if __name__ == '__main__':
    drive = get_drive_services()
    # Paste a small shared folder ID with a known file
    folder_id = input("Folder ID: ").strip()
    dest = input("Destination folder (e.g. ./tmp): ").strip() or './tmp'

    # Grab just the first file in the tree
    items = list(traverse_folder(drive, folder_id))
    if not items:
        print("No files found!")
        exit(1)
    file_meta, rel = items[0]
    print(f"Downloading {rel}...")
    download_file(drive, file_meta, rel, dest)
    print("Done!")
