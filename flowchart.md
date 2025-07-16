```mermaid
flowchart LR
  subgraph "UI Layer"
    CLI["CLI Interface"]
    GUI["GUI Interface"]
  end

  subgraph "App Layer"
    Manager["Download Manager"]
  end

  subgraph "Core Modules"
    Auth["Auth (auth.py)"]
    Traversal["Traversal (traversal.py)"]
    Downloader["Downloader (download.py)"]
    Logger["Logger (logger.py)"]
  end

  subgraph "Infra & External"
    DriveAPI["Google Drive API"]
    HTTP["HTTP Session / requests"]
    FS["Local File System"]
  end

  CLI -->|folder ID, path, threads| Manager
  GUI -->|folder ID, path, threads| Manager

  Manager --> Auth
  Manager --> Traversal
  Manager --> Downloader
  Manager --> Logger

  Auth --> DriveAPI
  Traversal --> DriveAPI
  Downloader --> HTTP
  Downloader --> FS
  Logger --> FS
