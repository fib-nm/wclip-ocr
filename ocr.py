import subprocess
from PIL import Image
import io

# Читает картинку из буфера обмена
def read_image():
    image = subprocess.check_output(["wl-paste", "--type", "image/png"])
    return image

# def copy_to_clipboard(text):
#     subprocess.run(["wl-copy"], input=text.encode())

def main():
    input()
    data = read_image()
    print("ok-1")

if __name__ == "__main__":
    main()
