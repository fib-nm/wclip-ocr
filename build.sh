#!/bin/bash

python -m venv .temp

source .temp/bin/activate

pip install pytesseract
pip install pillow
pip install pyinstaller

pyinstaller --onefile --name wclip-ocr --distpath . ocr.py

deactivate

rm -r .temp

exit