from PIL import Image
from rich import print

import pytesseract


def execute_ocr():
    print("Starting OCR")


pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

config_traning = "--tessdata-dir ./tess_data"

# Simple image to string
print(
    pytesseract.image_to_string(
        Image.open("./cupom.png"), lang="por", config=config_traning
    )
)

if __name__ == "__main__":
    execute_ocr()
