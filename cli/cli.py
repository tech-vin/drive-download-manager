# cli/cli.py

import argparse
from downloader.auth import get_drive_services
from downloader.manager import download_folder

def main():
    parser = argparse.ArgumentParser(description="Google Drive Folder Downloader")
    parser.add_argument('folder_id', help="Drive folder ID or shareable link")
    parser.add_argument('-o', '--output', default='.', help="Destination directory")
    parser.add_argument('-t', '--threads', type=int, default=4, help="Max parallel downloads")
    args = parser.parse_args()

    # Extract just the ID if a full URL was passed
    folder_id = args.folder_id.split('/')[-1].split('?')[0]
    drive_service = get_drive_services()
    download_folder(drive_service, folder_id, args.output, args.threads)

if __name__ == '__main__':
    main()
