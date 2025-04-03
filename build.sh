#!/bin/bash

python -m venv .temp

source .temp/bin/activate

pip install --no-index --find-links=./wheels pillow pyinstaller pytesseract

pyinstaller --onefile --name wclip-ocr ocr.py

ln -s dist/wclip-ocr

deactivate

rm -r .temp

exit