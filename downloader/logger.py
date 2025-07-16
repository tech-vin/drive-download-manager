# downloader/logger.py

import os
import logging

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'download_manager.log')

def setup_logger():
    """
    Configures and returns a logger for the download manager.
    Logs INFO and above to logs/download_manager.log.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger('download_manager')
    logger.setLevel(logging.INFO)

    # Avoid adding multiple handlers if this is called more than once
    if not logger.handlers:
        fh = logging.FileHandler(LOG_FILE)
        fh.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger
