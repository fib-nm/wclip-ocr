import subprocess
from PIL import Image
import io
import pytesseract
import shutil

def read_clipboard_image():
    try:
        image_data = subprocess.check_output(["wl-paste", "--type", "image/png"], stderr=subprocess.DEVNULL)
        return Image.open(io.BytesIO(image_data))
    except subprocess.CalledProcessError:
        return None

def write_clipboard_text(text):
    subprocess.run(["wl-copy", "--type", "text/plain;charset=utf-8", text])

def main():
    languages = pytesseract.get_languages(config='')
    print("Available languages: " + ", ".join(languages))
    current_language = 'eng'

    while True:
        print("Current language:", current_language)

        try:
            user_input = input()
        except EOFError:
            break
        
        if not user_input:
            image = read_clipboard_image()
            if image:
                print("Image successfully pasted!")

                text = pytesseract.image_to_string(image, lang=current_language)
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
        elif user_input in languages:
            current_language = user_input
        else:
            print("Unrecognized command. Enter available language, or press Enter to extract text from image.")

if __name__ == "__main__":
    main()