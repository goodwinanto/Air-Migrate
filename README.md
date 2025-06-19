# AirMigrate

**AirMigrate** is a cross-platform (Linux, macOS, Windows) Python desktop tool that safely transfers and organizes media files (photos, videos, etc.) from an iPhone to your PC. It works without iCloud, using [ifuse](https://github.com/libimobiledevice/ifuse) to mount your iPhone, and ensures zero data loss, privacy, and a clean user experience.

---

## ✨ Features

- **Scan iPhone DCIM folder:** Detect all Apple-style subfolders (e.g., 100APPLE, 101APPLE).
- **Media categorization:** Counts and previews for:
  - Photos (.HEIC)
  - Videos (.MOV)
  - Live Photos (.HEIC + .MOV)
  - Portraits, Panoramas, Raw/ProRAW, Cinematic, Slow-Mo, Time-lapse, Burst, Selfies, Screenshots, Screen Recordings, GIFs
- **Folder-level & total summary:** See counts and total size before transfer.
- **Flexible transfer:** Copy/move all or selected subfolders.
- **Destination options:**
  - Replicate iPhone folder structure or organize by type/date.
  - Pick or create a destination folder easily.
  - Warn if destination is not empty and check for enough free space.
- **Data integrity:**
  - Verifies each file by hash or size+timestamp.
  - Live Photos always transferred as pairs.
  - Moves only after successful copy and verification.
- **Error handling:** Robust detection of permission, device, or file system errors.
- **Progress feedback:** See per-folder and overall progress, with estimated time.
- **Privacy first:** No cloud, no analytics, no data sent anywhere.

---

## 🖥️ How It Works

1. **Mount your iPhone** with ifuse at `~/iPhone` (or your chosen mount point).
2. **Start AirMigrate:** Launch the app and select your destination folder (or let it create one for you).
3. **Preview:** See a categorized summary of your iPhone media.
4. **Choose:** Pick to copy/move all or selected folders, and your preferred organization style.
5. **Transfer:** AirMigrate safely transfers (and optionally moves) files, verifying each one.
6. **Complete:** Get a summary of what was copied, skipped, or failed.

---

## 📦 Project Structure

```
AirMigrate/
├── gui.py            # Tkinter-based GUI interface
├── media_handler.py  # Scanning, classification, copy/move logic
├── utils.py          # Helper functions (e.g., default folder, hash)
├── main.py           # Launches the GUI
└── README.md         # This file
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **ifuse** (installation varies by OS)
- **Tkinter** (usually included with Python)
- **pip** for dependencies

### Basic Setup

1. **Clone this repo** (or download the files).
2. **Mount your iPhone** using ifuse:
   ```sh
   mkdir -p ~/iPhone
   ifuse ~/iPhone
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run AirMigrate:**
   ```sh
   python main.py
   ```

---

## ⚠️ Safety & Data Integrity

- Always **copy first, verify**, then move/delete originals.
- All files are checked for integrity (hash or size+timestamp).
- Live Photos are always paired and transferred together.
- No files are deleted unless you explicitly choose **Move** and verification passes.

---

## 🧩 Advanced & Optional

- **Simulation mode:** Preview what will be transferred without copying.
- **Export logs:** Optionally export a summary/log of transfers.
- **CLI version:** (planned) for scripting or automation.

---

## 🛠️ Contributing

Contributions and feedback are welcome!  
See [CONTRIBUTING.md](CONTRIBUTING.md) for details (coming soon).

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for full text.

---

## 💬 Support

For issues or feature requests, please open an issue on GitHub.

---

**AirMigrate** — The safe, open-source way to move your iPhone photos and videos to your computer, with zero data loss.