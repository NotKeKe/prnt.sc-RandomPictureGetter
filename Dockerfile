FROM python:3.13.5-slim

WORKDIR /app

COPY . .

# time, ocr, pip
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime && \
    echo "Asia/Taipei" > /etc/timezone && \
    apt update && \
    apt install -y tesseract-ocr && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt