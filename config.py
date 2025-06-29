Enable_OCR = True
logging_level = 'INFO' # logging_level can be set to DEBUG, INFO, WARNING, ERROR or CRITICAL





























'''
!請不要更改以下內容!
!Please do not modify the following content!
'''
import logging
import shutil
from src.logger import logger

level_map = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}
logger.setLevel(level_map.get(logging_level.upper(), logging.INFO))

if not shutil.which('tesseract') and Enable_OCR:
    logger.error('請先安裝 tesseract，或者關閉 config.py 中的 Enable_OCR 設置。\n前往 https://github.com/tesseract-ocr/tesseract/releases 進行安裝')
    Enable_OCR = False