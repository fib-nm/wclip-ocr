import subprocess
from PIL import Image
import io
import pytesseract
import shutil

def read_clipboard_image():
    try:
        image_data = subprocess.check_output(["wl-paste", "--type", "image/jpg"])
        return Image.open(io.BytesIO(image_data))
    except subprocess.CalledProcessError:
        return None

def write_clipboard_text(text):
    subprocess.run(["wl-copy", "--type", "text/plain;charset=utf-8", text])

def main():
    print("Press Enter to extract text from the image in the clipboard (Ctrl-D to exit).")
    while True:
        try:
            input()
        except EOFError:
            break

        image = read_clipboard_image()
        if image:
            print("Image successfully pasted!")

            text = pytesseract.image_to_string(image)
            print("Text successfully extracted!")

            write_clipboard_text(text)
            print("Extracted text copied to the clipboard!")

            terminal_width = shutil.get_terminal_size().columns
            print("Extracted text:")
            print("=" * terminal_width)
            print(text)
            print("=" * terminal_width)
        else:
            print("No image found in the clipboard!")

if __name__ == "__main__":
    main()