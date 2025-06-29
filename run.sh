#!/bin/bash

# 偵測作業系統
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     OS_TYPE=Linux;;
    Darwin*)    OS_TYPE=Mac;;
    *)          OS_TYPE="UNKNOWN:${unameOut}"
esac

# 根據系統進行安裝
if [ "$OS_TYPE" = "Mac" ]; then
    echo "使用 Homebrew 安裝 Tesseract..."
    if ! command -v brew &> /dev/null; then
        echo "❌ 找不到 Homebrew，請先安裝 Homebrew！"
        exit 1
    fi
    brew install tesseract
    echo "✅ Tesseract 安裝完成！"
elif [ "$OS_TYPE" = "Linux" ]; then
    echo "使用 apt 安裝 Tesseract..."

    # 檢查是否為 root
    if [ "$(id -u)" -eq 0 ]; then
        APT_PREFIX=""
    else
        APT_PREFIX="sudo"
    fi

    $APT_PREFIX apt update
    $APT_PREFIX apt install -y tesseract-ocr
    
    echo "✅ Tesseract 安裝完成！"
fi

pip install -r requirements.txt
pm2 start main.py --name "prnt_sc_getter" --interpreter python3