# wclip-ocr
wclip-ocr is a console app for Wayland that can extract text from images stored in clipboard.

# Dependencies
1. wl-clipboard
2. tesseract

# Installation
1. Make sure that you installed dependencies and that they are accessable from PARH.
2. Clone the repository
3. Run `build.sh` script. It will
    1. Install python dependencies of a project and PyInstaller in a venv
    2. Create binary using PyInstaller
    3. Delete venv

After running the script you will have binary located in dist/wclip-ocr/wclip-ocr.

# Usage
1. 