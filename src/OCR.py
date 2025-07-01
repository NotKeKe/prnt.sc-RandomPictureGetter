from PIL import Image
import pytesseract

from src.logger import logger

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def check_img(file_path: str) -> bool:
    logger.debug('正在檢查圖片...')
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image, lang="eng")
    text = text.replace('\n', '').replace(' ', '')
    return ('''The image you are
    requesting does not exist
    or is no longer available'''.replace('\n', '').replace(' ', '') in text)