import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_logger(name='yin-xi', log_dir='logs'):
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # 建立 handler：每天 0 點自動 rotate，保留 7 天
    log_file = f"{log_dir}/{name}.log"
    handler = TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=10, encoding='utf-8'
    )
    handler.suffix = "%Y-%m-%d"  # 自動加入日期後綴

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(logging.StreamHandler())  # 同時印出到終端機

    return logger

logger = setup_logger()
