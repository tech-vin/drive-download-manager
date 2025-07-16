# downloader/traversal.py

import os

def list_files_in_folder(drive, folder_id):
    """
    Yield metadata dicts (id, name, mimeType) for each item directly in `folder_id`.
    """
    page_token = None
    query = f"'{folder_id}' in parents and trashed=false"
    while True:
        response = drive.files().list(
            q=query,
            fields='nextPageToken, files(id, name, mimeType)',
            pageSize=1000,
            pageToken=page_token
        ).execute()
        for item in response.get('files', []):
            yield item
        page_token = response.get('nextPageToken')
        if not page_token:
            break

def traverse_folder(drive, folder_id, path_prefix=''):
    """
    Recursively walk `folder_id`, yielding tuples:
      (file_meta, relative_local_path)
    """
    for item in list_files_in_folder(drive, folder_id):
        # Build the path where this item should live
        rel_path = os.path.join(path_prefix, item['name'])
        
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            # Recurse into subfolder
            yield from traverse_folder(drive, item['id'], rel_path)
        else:
            # It’s a file; yield its metadata + where to save it
            yield item, rel_path
