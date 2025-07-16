# Google Drive Download Manager

A robust Python application to download large shared Google Drive folders (100GB+) while preserving the original folder hierarchy. Supports resumable transfers, multi-threaded downloads, progress reporting, and both CLI and GUI interfaces.

---

## 🚀 Features

* **Recursive Traversal**: Download all files and nested subfolders from a shared Drive folder.
* **Resumable Downloads**: Automatically resume interrupted downloads using Drive’s resumable API.
* **Multi-Threaded**: Configure parallel downloads for faster performance.
* **Progress Tracking**: Per-file tqdm progress bars in CLI and real-time log output in GUI.
* **CLI & GUI**: Flexible command-line interface and an optional PySimpleGUI desktop UI.
* **Logging**: Records completed, skipped, and failed downloads in `logs/download_manager.log`.
* **Easy Setup**: Simple OAuth2 flow with cached credentials.

---

## 📦 Tech Stack

* **Language**: Python 3.7+
* **APIs**: Google Drive API (v3)
* **HTTP**: `requests` / `google-auth-httplib2`
* **CLI**: `argparse`
* **GUI**: `PySimpleGUI`
* **Concurrency**: `concurrent.futures.ThreadPoolExecutor`
* **Progress Bars**: `tqdm`
* **Logging**: Python’s built-in `logging`

---

## 🛠 Prerequisites

* Python 3.7 or newer
* A Google account with access to the shared Drive folders
* Google Cloud project with Drive API enabled

---

## 📁 Project Structure

```
drive_downloader/
├── credentials.json           # OAuth2 client secrets (download from GCP)
├── token.pickle               # Auto-generated after auth
├── drive_downloader.py        # (Optional) master launcher
├── requirements.txt           # Pinned dependencies
├── setup.py                   # Package setup (if used)
├── README.md                  # This file
├── logs/
│   └── download_manager.log   # Download events log
├── downloader/
│   ├── __init__.py
│   ├── auth.py                # OAuth flow & Drive service
│   ├── traversal.py           # Recursive folder listing
│   ├── download.py            # Resumable download logic
│   ├── manager.py             # Orchestration & threading
│   └── logger.py              # Logger configuration
├── cli/
│   ├── __init__.py
│   └── cli.py                 # CLI entry point
├── gui/
│   ├── __init__.py
│   └── app.py                 # PySimpleGUI window
└── tests/
    ├── __init__.py            # package marker
    ├── test_auth.py           # OAuth smoke test
    ├── test_traversal.py      # Folder traversal test
    └── test_download.py       # Single-file download test
```

---

## 🔧 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone <repo_url>
   cd drive_downloader
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   # venv\Scripts\activate     # Windows PowerShell
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Google Cloud Setup**

   * Go to [Google Cloud Console](https://console.cloud.google.com/) and select or create a project.
   * Enable **Google Drive API** under **APIs & Services → Library**.
   * Configure the **OAuth consent screen**:

     * User Type: **External**
     * Fill **App name**, **support email**, and add yourself under **Test users**.
   * Create credentials: **APIs & Services → Credentials → Create Credentials → OAuth client ID**

     * Application type: **Desktop app**
     * Download the JSON, rename to `credentials.json`, and place in the project root.

5. **First-time Authentication**

   ```bash
   python -m tests.test_auth
   ```

   * A browser window will open for consent. After approval, `token.pickle` appears.

---

## ▶️ Running Tests

* **Traversal**:

  ```bash
  python tests/test_traversal.py
  ```
* **Download**:

  ```bash
  python tests/test_download.py
  ```

---

## 📖 Usage

### CLI

```bash
python -m cli.cli <FOLDER_ID_OR_LINK> \
    -o ./downloads -t 6
```

* `<FOLDER_ID_OR_LINK>`: Google Drive folder ID or shareable link
* `-o`: Destination directory (default: current directory)
* `-t`: Number of parallel download threads (default: 4)

### GUI

```bash
python -m gui.app
```

1. Paste the Drive folder ID or link.
2. Choose output directory.
3. Select thread count.
4. Click **Download** and watch real‑time logs.

---

## 📊 Logging

Download events are recorded in `logs/download_manager.log`:

```
2025-07-16 18:32:10 INFO: Starting download of 42 files from folder XYZ
2025-07-16 18:32:30 INFO: ✔ Completed: file1.zip
2025-07-16 18:33:00 ERROR: ✖ Failed: file2.iso – Connection reset
...
```

---

## 🏗 Architecture Overview

* **Auth** (`auth.py`): OAuth2 flow → `drive` service object.
* **Traversal** (`traversal.py`): Lists folder contents recursively.
* **Download** (`download.py`): Resumable chunked download via `MediaIoBaseDownload`.
* **Manager** (`manager.py`): Gathers tasks, runs multi‑threaded downloads, logs results.
* **CLI** (`cli.py`) & **GUI** (`app.py`): User-facing entry points.

---

## 🤝 Contributing

1. Fork this repo.
2. Create a branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m "Add YourFeature"`.
4. Push: `git push origin feature/YourFeature`.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.
