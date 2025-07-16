# Contributing to the GUI Module

This document outlines guidelines and best practices for contributing to the `gui/` portion of the Google Drive Download Manager.

---

## 🛠️ Setup for GUI Development

1. **Clone the repository & enter the project root**

   ```bash
   git clone <repo_url>
   cd drive_downloader
   ```

2. **Ensure you have a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   # venv\Scripts\activate     # Windows PowerShell
   ```

3. **Install dependencies** (GUI requires PySimpleGUI)

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Verify GUI runs**

   ```bash
   python -m gui.app
   ```

---

## 🐛 Known Issues & Debugging

* **TclError on macOS**:

  * Issue: PhotoImage can’t load embedded PNG, causing `couldn't recognize image data`.
  * Workaround: In `gui/app.py`, set `finalize=False` and/or supply a GIF icon:

    ```python
    window = sg.Window(
        'Google Drive Downloader', layout,
        icon='path/to/icon.gif',
        finalize=False
    )
    ```

* **Autofinalize behavior**:

  * Avoid calling `Finalize()` implicitly. Ensure your event loop uses `window.read(timeout=...)` before any image operations.

* **Long–running downloads blocking UI**:

  * The download must run in a background thread. Use `threading.Thread(..., daemon=True)` and `window.write_event_value(...)` to push progress or completion events back into the main UI thread.

---

## ✍️ Coding Guidelines

* **PEP 8** compliance for all new code. Use an autoformatter (e.g. `black`) where possible.
* **Single-responsibility**: UI components (`app.py`) should only handle layout and event dispatch. Business logic (traversal, download, logging) must reside in `downloader/` modules.
* **Thread-safety**: Never call blocking I/O on the main thread. Use `Window.write_event_value` to communicate between threads.
* **Minimal dependencies**: Limit GUI-specific packages to `PySimpleGUI` only.

---

## ✅ Testing Your Changes

1. **Unit tests**: Add tests in `tests/` for any new utility functions in the GUI (e.g., link parsing, settings validation).
2. **Manual QA**:

   * Run the GUI on macOS and Linux to ensure no platform-specific errors.
   * Test both success and failure flows:

     * Valid folder download
     * Invalid folder ID (error popup)
     * Interrupted download → resume
3. **CI Integration**: If adding automated GUI tests (e.g. with `pytest-qt` or `pytest-tkinter`), update CI config accordingly.

---

## 🚀 How to Submit

1. **Fork** the repo & create a feature branch:

   ```bash
   git checkout -b feature/gui-enhancement
   ```
2. **Implement** your changes and **document** any new behaviors or settings.
3. **Commit** with descriptive messages:

   ```bash
   git commit -m "Fix macOS icon load issue in GUI"
   ```
4. **Push** to your fork and open a Pull Request, referring to this Contribute doc.
5. **Include** screenshots or GIFs for UI changes.

---

Thank you for helping improve the GUI! 🎉
