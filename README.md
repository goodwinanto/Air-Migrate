# AirMigrate

![Project Status: In Progress](https://img.shields.io/badge/status-in--progress-yellow)

**AirMigrate** is a cross-platform Python desktop application designed to safely transfer and organize media files (photos and videos) from an iPhone to your computer without using iCloud. It leverages [ifuse](https://github.com/libimobiledevice/ifuse) to mount your iPhone's file system and provides a robust, privacy-focused workflow for copying or moving files.

---

## Project Status

This project is currently **in progress**. Functionality and documentation are evolving.  
Expect bugs and incomplete features.

---

## Features

- **Scan & Summarize:** Scans the iPhone DCIM folder for all media (photos, videos, Live Photos, Portraits, Panoramas, RAW, etc.) and provides a folder-level and total summary before transferring.
- **Media Classification:** Categorizes media types for flexible organization.
- **Copy or Move:** Allows you to either copy or move media files, with robust verification (hash-based) to ensure data integrity.
- **Live Photo Handling:** Handles paired files (HEIC+MOV) for Live Photos.
- **Progress Feedback:** Shows progress bar and per-file status during transfer.
- **Error Handling:** Logs every operation, error, hash mismatch, and summary in a log file (`airmigrate.log`).
- **Privacy Respecting:** No cloud, no analytics, all processing is local.

---

## Typical Workflow

1. **Mount your iPhone** using [ifuse](https://github.com/libimobiledevice/ifuse).
2. **Launch AirMigrate** and select your source (iPhone/DCIM) and destination folders.
3. **Scan and review** your media files and summary.
4. **Choose Copy or Move**, then start the operation.
5. **Monitor progress** and review the log for details.

---

## Requirements

- Python 3.7+
- [ifuse](https://github.com/libimobiledevice/ifuse) (for mounting iPhone's DCIM folder)
- Tkinter (for GUI, usually included with Python)
- Standard Python libraries (`os`, `shutil`, `hashlib`, etc.)

---

## Installation

1. **Clone this repository:**
    ```sh
    git clone https://github.com/<your-username>/aptivate.git
    cd aptivate
    ```

2. **(Optional) Create a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    - For most systems, Tkinter is included.
    - If missing:  
      - Ubuntu: `sudo apt-get install python3-tk`
      - macOS: Included with Python from python.org or Homebrew.

---

## Usage

1. **Mount your iPhone:**
    ```sh
    ifuse /mnt/iphone
    ```
    (Replace `/mnt/iphone` with your desired mount point.)

2. **Run the app:**
    ```sh
    python main.py
    ```

3. **Follow the GUI prompts** to select your source and destination folders, scan, and transfer files.

---

## Logging

All operations, errors, and hash verifications are logged to `airmigrate.log` in the working directory.  
Review this log for troubleshooting or to audit the transfer process.

---

## Contributing

Pull requests and issues are welcome!  
Please note that this project is **in progress** and may change rapidly.

---

## License

MIT License

---

## Disclaimer

This project is not affiliated with Apple Inc.  
Use at your own risk—always verify your backups before deleting originals.
