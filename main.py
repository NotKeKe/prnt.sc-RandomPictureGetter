import asyncio

from src.abcdef import run
from src.database import initialize_db
from src.logger import logger

async def main_run():
    await initialize_db()
    while True:
        await run()
        await asyncio.sleep(2)

async def main():
    await asyncio.create_task(main_run())

logger.info('prnt.sc getter 開始運行!')
logger.info('儲存檔名格式為: {prnt.sc code}-{imgur code}')
asyncio.run(main())