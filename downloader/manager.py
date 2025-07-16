# downloader/manager.py

import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from downloader.traversal import traverse_folder
from downloader.download import download_file
from downloader.logger import setup_logger

def download_folder(service, folder_id, dest_root, max_workers=4):
    """
    Orchestrates recursive traversal and parallel downloads.
    """
    logger = setup_logger()
    os.makedirs(dest_root, exist_ok=True)

    # Gather all (meta, relative path) pairs
    tasks = list(traverse_folder(service, folder_id))
    total_files = len(tasks)
    logger.info(f"Starting download: {total_files} files from folder {folder_id}")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_task = {
            executor.submit(download_file, service, meta, rel, dest_root): (meta, rel)
            for meta, rel in tasks
        }

        for future in as_completed(future_to_task):
            meta, rel = future_to_task[future]
            try:
                future.result()
                logger.info(f"✔ Completed: {rel}")
            except Exception as exc:
                logger.error(f"✖ Failed: {rel} {exc}")

    logger.info("All download tasks finished.")
