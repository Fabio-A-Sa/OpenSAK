# OpenSAK — Open Source geocaching management tool

A cross-platform geocaching management tool for **Linux**, **Windows** and **macOS** — a modern successor to GSAK, built in Python.

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org)
[![PySide6](https://img.shields.io/badge/GUI-PySide6-green)](https://doc.qt.io/qtforpython/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Beta-orange)](https://github.com/AgreeDK/opensak)

> ⚠️ **Hobby project disclaimer** — OpenSAK is developed in spare time with no guaranteed update schedule, bug fix timeline, or support commitment. Pull requests and contributions are warmly welcomed!

---

## Features

### Import & Database

* 📥 **Import** GPX files and Pocket Query ZIP files from Geocaching.com
* 🗄️ **Multiple databases** — keep e.g. Zealand, Bornholm and Cyprus separate
* 📍 **Centre point per database** — distances calculated from your chosen starting point
* ✅ **Update finds** from a reference database (e.g. "My Finds" PQ)

### Viewing & Navigation

* 🗺️ **Interactive map** with OpenStreetMap and colour-coded cache pins
* 🔍 **Advanced filter dialog** — 3 tabs: General, Dates and Attributes
* 📊 **Configurable columns** — 17+ columns can be toggled on/off
* 🎨 **Status icons** in the list — ✅ found, ❌ DNF, 🔒 archived, ⚠️ unavailable
* 🔗 **Click GC code** → opens cache page on geocaching.com
* 🗺️ **Click coordinates** → opens in Google Maps or OpenStreetMap

### Cache Details

* 📋 **Cache detail panel** — description, hints and logs
* 🔓 **ROT13 hint decoding** — one click to decode / re-hide
* 🔍 **Search in logs** — real-time search with match highlighting
* ✏️ **Add / edit / delete caches** manually (Waypoint CRUD)

### GPS Export

* 📡 **Send to GPS** — export caches directly to a Garmin device via USB
* 🗑️ **Delete existing GPX files** on device before upload (with confirmation)
* 💾 **Save as GPX file** — export to any local path

### Right-click Menu

* 🌐 Open on geocaching.com
* 🗺️ Open in map app (Google Maps / OpenStreetMap)
* 📋 Copy GC code / coordinates
* ☑ Mark as found / not found

### Language Support

* 🌍 **Danish and English** built in — easily extensible to other languages
* 🔄 **Language switcher** in Settings dialog (takes effect on next restart)

---

## Known Limitations (Beta)

* Favourite points cannot be imported from GPX/PQ files
* No Geocaching.com Live API integration (planned)
* No HTML/PDF report/export function yet (planned)
* GPS auto-detection may not work on all Linux distros
* macOS and Windows not yet tested — feedback welcome!

---

## System Requirements

| Platform | Requirement |
|---|---|
| **Linux** | Ubuntu 20.04+ / Linux Mint 20+ / Debian 11+ |
| **Windows** | Windows 10 or newer |
| **macOS** | macOS 11 (Big Sur) or newer |
| **Python** | 3.10 or newer |
| **Disk space** | Approx. 500 MB (incl. PySide6) |

---

## Installation

### Linux (Ubuntu / Linux Mint / Debian)

```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip libxcb-cursor0

cd ~
git clone https://github.com/AgreeDK/opensak.git
cd opensak

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python run.py
```

---

### Windows

**Install Python 3.10+** from [python.org](https://www.python.org/downloads/) — make sure to check **"Add Python to PATH"**

**Install Git** from [git-scm.com](https://git-scm.com/download/win)

```powershell
cd $env:USERPROFILE
git clone https://github.com/AgreeDK/opensak.git
cd opensak
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

---

### macOS

> ⚠️ macOS has not been tested yet. Feedback is very welcome!

```bash
brew install python git

cd ~
git clone https://github.com/AgreeDK/opensak.git
cd opensak
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

---

## Getting Started — First Use

### 1. Get a Pocket Query from Geocaching.com

1. Log in at [geocaching.com](https://www.geocaching.com)
2. Go to **Pocket Queries** under your profile menu
3. Download a Pocket Query as a `.zip` file

### 2. Import into OpenSAK

1. Start OpenSAK with `python run.py`
2. Click **Import GPX / PQ zip** in the menu bar
3. Select your `.zip` file and click **Import**

### 3. Set your centre point

1. Go to **Tools → Settings**
2. Enter your home coordinates (latitude / longitude)
3. Choose your preferred map app (Google Maps or OpenStreetMap)

### 4. Filter and find caches

* **Quick filter** — dropdown at the top of the window
* **Advanced filter** — click 🔍 **Filter** in the toolbar (Ctrl+F)
  * General, Dates and ~70 Groundspeak attributes
  * Save filter profiles for reuse

---

## Update Found Caches from "My Finds"

1. Download your **"My Finds"** Pocket Query from geocaching.com
2. Create a new database called "My Finds" in OpenSAK
3. Import the My Finds ZIP file into that database
4. Switch back to the database you want to update
5. Go to **Tools → Update finds from reference database**

---

## Send Caches to GPS Device

1. Connect your Garmin GPS via USB
2. Go to **GPS → Send to GPS** (Ctrl+G)
3. Click **Scan** to detect the device automatically
4. Optionally enable **"Delete existing GPX files on device"**
5. Click **Send**

---

## Update to Latest Version

```bash
cd ~/opensak
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows

git pull origin main
pip install -r requirements.txt
python run.py
```

---

## Report a Bug

Use [GitHub Issues](https://github.com/AgreeDK/opensak/issues) and include:

* Your platform (Linux/Windows/macOS + version)
* Python version: `python3 --version`
* Error message from the terminal

---

## Project Structure

```
opensak/
├── run.py                              # Start the application from here
├── requirements.txt
├── src/opensak/
│   ├── app.py
│   ├── config.py
│   ├── lang/                           # i18n — da.py, en.py, fr.py + __init__.py
│   ├── db/
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── manager.py
│   │   └── found_updater.py
│   ├── importer/
│   ├── filters/
│   │   └── engine.py                   # 18 filter types with AND/OR logic
│   ├── gps/
│   │   └── garmin.py                   # Garmin detection + GPX generator
│   └── gui/
│       ├── mainwindow.py
│       ├── cache_table.py
│       ├── cache_detail.py
│       ├── map_widget.py
│       ├── settings.py
│       └── dialogs/
│           ├── filter_dialog.py        # Advanced filter (3 tabs)
│           ├── import_dialog.py
│           ├── waypoint_dialog.py
│           ├── column_dialog.py
│           ├── database_dialog.py
│           ├── found_dialog.py
│           ├── gps_dialog.py           # GPS export + delete dialog
│           └── settings_dialog.py
└── tests/
```

---

## Roadmap

* HTML/PDF reports and statistics
* Favourite points (requires Geocaching.com API)
* More languages (German, Swedish, …)
* Windows installer (.exe)
* Linux AppImage
* GitHub Actions CI/CD pipeline

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Thanks to

* [OpenStreetMap](https://www.openstreetmap.org) for map data
* [Leaflet.js](https://leafletjs.com) for the map library
* [PySide6 / Qt](https://www.qt.io) for the GUI framework
* [SQLAlchemy](https://www.sqlalchemy.org) for the database layer
* Everyone who has tested and given feedback!
