# wclip-ocr
wclip-ocr is a console app for Wayland that can extract text from images stored in clipboard.

# Dependencies
1. wl-clipboard
2. tesseract
3. pip
4. python

# Installation
1. Install all dependencies
2. Clone the repository and cd into it
```bash
git clone https://github.com/fib-nm/wclip-ocr.git
cd wclip-ocr
```
3. Run `build.sh` script
```bash
./build.sh
```

After running the script you will have binary `wclip-ocr` in `wclip-ocr`.

# Usage
Launch `wclip-ocr` script.
```bash
./wclip-ocr
```

To set the language, type its name in the command line and press `Enter` (names of the available languages are printed when the command starts).

To extract text from image in the clipboard just press `Enter`.

To close application, press `Ctrl+D`.

# Tips
Since program uses tesseract for OCR, to get new languages you will need to install `tesseract-data-lang` packages from your system's repository.

Program not only prints extracted text, but also copies it to your clipboard, so you can immediately paste it wherever you need.

## Making binary globally callable

If you don't want to write full path to the binary every time you use the program, you can add alias for it to your `.bashrc` file.
```bash
alias ocr='/path/to/wclip-ocr/wclip-ocr'
```
