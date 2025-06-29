from bs4 import BeautifulSoup
import aiohttp
import random
import string
import aiofiles
import asyncio
from pathlib import Path

from src.database import code_exists, save_code
from src.logger import logger

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

async def run():
    # 生成隨機 code
    def generate_random_code(length=6):
        """
        產生一個指定長度、由英文大小寫字母和數字組成的隨機代碼。
        """
        characters = string.ascii_letters + string.digits

        random_code = ''.join(random.choice(characters) for i in range(length))
        return random_code
    
    code = generate_random_code()
    
    if ( await code_exists(code) ):
        while True:
            logger.debug(f'{code} is in codes list, trying to regerenate a code...')

            code = generate_random_code()
            if ( await code_exists(code) ): 
                await asyncio.sleep(1)
            else:
                break

    await save_code(code)
    logger.debug(f'Current code: {code}')

    url = f'https://prnt.sc/{code}'
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url, headers=header)
        if resp.status != 200: return

        html_content = await resp.text()
    # 取得圖片連結 (imgur)
    soup = BeautifulSoup(html_content, 'html.parser')
    image_meta_tag = soup.find('meta', {'property': 'og:image'})

    if image_meta_tag:
        image_url = image_meta_tag['content']
        if image_url:
            if image_url.startswith('//'):
                logger.debug('找不到圖片網址 (地址 starts with //)')
                return 
            else:
                logger.debug(f"找到的圖片網址: {image_url}")

        async def download_img(image_url: str):
            # 構建 URL
            image_id = image_url.split('/')[-1]
            direct_url = f"https://i.imgur.com/{image_id}"
            referer_url = f"https://imgur.com/{image_id}"
                
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": referer_url
                }
                
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(direct_url, headers=headers) as response:
                        response.raise_for_status()
                        
                        if 'image' in response.headers.get('Content-Type', ''):
                            filename = f"{image_id}"
                            Path('imgs').mkdir(parents=True, exist_ok=True)
                            async with aiofiles.open(f'./imgs/{code}-{filename}', 'wb') as f:
                                await f.write(await response.read())
                            logger.info(f"圖片已成功下載：{code}-{filename} / 圖片連結: {direct_url}")
                        else:
                            logger.debug("下載失敗：返回內容不是圖片")
            
            except aiohttp.ClientError as e:
                logger.error(f"下載失敗：{e}")

        await download_img(image_url)
    else:
        logger.debug("沒有找到圖片網址 (no og:image)")