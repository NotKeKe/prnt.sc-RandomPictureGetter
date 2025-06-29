# prnt.sc Random Image Downloader
<p align="center">
  <a href="https://github.com/NotKeKe/prnt.sc-RandomPictureGetter">
    <img src="https://img.shields.io/github/stars/NotKeKe/prnt.sc-RandomPictureGetter?style=social" />
  </a>
</p>

📖 [中文](./assests/README_zh_TW.md)

## 📌 Introduction
This project can randomly generate codes on prnt.sc and download the images.

## 🚀 Usage
* Install [Python3](https://www.python.org/downloads/)

### How to use
1. **Windows**
   - Directly use the `run.bat` file, or use the second method below.
2. **Using pm2**
   - Install [Node.js](https://nodejs.org/en/download)
   - Install [pm2](https://pm2.keymetrics.io/)
     - `npm install pm2 -g`
   - Navigate to the project directory
   - Run the `run.sh` file in PowerShell or your preferred terminal

## 🖼️ Image Location
Downloaded images will be in the `./imgs` folder

## OCR (Optical Character Recognition)
This project integrates [tesseract-ocr](https://github.com/tesseract-ocr/tesseract), which can be enabled/disabled in `config.py`

### Installation
1. **Windows**
   - Go to [tesseract-ocr releases](https://github.com/tesseract-ocr/tesseract/releases), find the version with `.exe` for download ([latest version](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe) at the time of writing)
2. **macOS/Linux**
   - No action required, I've included tesseract installation commands in `run.sh`

## ⚠️ Disclaimer
This project is for **educational purposes only**. Users must assess the risks themselves and bear all consequences resulting from its use.

## 💬 Author's Note
Honestly, I'm not sure why you'd need this<br>
I don't even know why I made this<br>
But anyway, I suddenly saw prnt.sc on YouTube<br>
And ended up creating this out of boredom<br>
Maybe they have an API? Or something similar<br>
Since this was casually made, the code might be messy - sorry about that!<br>
<br>
Oh, the reason I used OCR is because<br>
I found it sometimes downloads "image not found" placeholder images<br>
I'm not sure if there's a pattern to avoid them, but I was lazy<br>
So I just implemented OCR to detect text matching `The image you are requesting does not exist...` and delete those files<br>
