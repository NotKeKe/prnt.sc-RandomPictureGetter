<div align="center">

# prnt.sc Random Image Downloader

![Stars](https://img.shields.io/github/stars/NotKeKe/prnt.sc-RandomPictureGetter?style=social)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<br>
[![Docs](https://img.shields.io/badge/Docs-繁體中文-blue.svg)](README_zh_TW.md) 
[![Docs](https://img.shields.io/badge/Docs-English-blue.svg)](../README.md)

</div>

## 📌 簡介
此專案可以從 prnt.sc 上隨機窮舉代碼，並將圖片下來

## 🚀 使用方式
* 安裝 [python3](https://www.python.org/downloads/)
### 使用
1. **windows**
- 直接使用 `run.bat` 檔案，或者使用接下來的第二個方法。
2. **使用 pm2**
- 安裝 [node.js](https://nodejs.org/zh-tw/download)
- 安裝 [pm2](https://pm2.keymetrics.io/)
    - `npm install pm2 -g`
- 進入當此專案所在的目錄
- 在 powershell 或者你喜歡的終端中，運行 `run.sh` 檔案

## 🖼️ 圖片位置
下載下來的圖片，會在 `./imgs` 資料夾當中

## OCR 光學辨識
此專案結合了 [tesseract-ocr](https://github.com/tesseract-ocr/tesseract)，可以在 `config.py` 中將他啟用/禁用
### 安裝
1. **windows**
- 前往 [tesseract-ocr releases](https://github.com/tesseract-ocr/tesseract/releases)，找到有 `.exe` 的版本進行下載 (製作此專案時看到的[最新版本](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe))
2. **macOS / Linux**
- 無需進行任何操作，我已經在 `run.sh` 當中加入了 tesseract 的安裝指令

## ⚠️ 免責聲明
本專案僅供**學習用途**，使用者需自行判斷風險並承擔使用所產生之一切後果。

## 📄 授權
- [LICENSE-MIT](LICENSE)

## 💬 我要說的話
呃說實話我不知道為什麼你會需要這個<br>
我也不知道為什麼我要寫這個<br>
但反正我就突然在yt上看到 prnt.sc<br>
然後就無聊寫出來了<br>
或許他本身有提供 api ? 之類的<br>
阿因為我這是隨便做出來的 所以代碼可能有點亂 見諒w<br>
<br>
喔對我用到OCR的原因是因為<br>
我發現他會下載到一些寫說圖片不存在 的圖片<br>
我不確定他會不會其實有什麼規律可以找 但我懶w<br>
所以就直接去搞了個 OCR 辨識，如果辨識出是`The image you are requesting does not exist...` 的 就直接把下載下來的檔案刪掉<br>