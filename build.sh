#!/bin/bash

python -m venv .temp

source .temp/bin/activate

pip install pytesseract
pip install pillow
pip install pyinstaller

pyinstaller ocr.py

deactivate

rm -r .temp

exit