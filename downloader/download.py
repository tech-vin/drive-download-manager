# downloader/download.py

import os
from tqdm import tqdm
from google.auth.transport.requests import AuthorizedSession

def _get_authorized_session(service):
    """
    Grab the underlying credentials from the Drive service
    and wrap them in a requests‐style session.
    """
    creds = service._http.credentials
    return AuthorizedSession(creds)

def get_download_url(file_id: str) -> str:
    """
    Direct “alt=media” URL for downloading non‐Google‐Docs files.
    """
    return f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"

def download_file(service, file_meta: dict, rel_path: str, dest_root: str):
    """
    Download a single file with resume support and a tqdm progress bar.
    
    Args:
      service: authorized Drive API service
      file_meta: metadata dict (must have 'id' and 'name')
      rel_path: path relative to dest_root (e.g. 'sub/dir/file.zip')
      dest_root: local root directory to save into
    """
    session = _get_authorized_session(service)
    url = get_download_url(file_meta['id'])
    dest_path = os.path.join(dest_root, rel_path)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Determine resume offset
    mode = 'wb'
    headers = {}
    existing = 0
    if os.path.exists(dest_path):
        existing = os.path.getsize(dest_path)
        headers['Range'] = f"bytes={existing}-"
        mode = 'ab'

    # Figure out total size
    head = session.head(url)
    head.raise_for_status()
    if 'Content-Range' in head.headers:
        # e.g. "bytes 1024-2047/4096"
        total = int(head.headers['Content-Range'].split('/')[-1])
    else:
        total = int(head.headers.get('Content-Length', 0))

    # Stream & write
    resp = session.get(url, headers=headers, stream=True)
    resp.raise_for_status()

    with open(dest_path, mode) as f, tqdm(
        total=total, initial=existing,
        unit='B', unit_scale=True,
        desc=rel_path,
        leave=False
    ) as pbar:
        for chunk in resp.iter_content(chunk_size=32*1024):
            if not chunk:
                continue
            f.write(chunk)
            pbar.update(len(chunk))
