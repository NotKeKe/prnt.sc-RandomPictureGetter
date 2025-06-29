import aiosqlite

from src.logger import logger

db_name = 'codes.db'

async def initialize_db():
    """
    異步初始化資料庫：建立一個用於儲存代碼的表，如果它還不存在的話。
    """
    async with aiosqlite.connect(db_name) as db:
        # 使用 CREATE TABLE IF NOT EXISTS 避免重複創建
        # code TEXT PRIMARY KEY UNIQUE 確保 code 欄位是唯一的，且會自動建立索引，加速查詢
        await db.execute('''
            CREATE TABLE IF NOT EXISTS generated_codes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()

async def code_exists(code):
    """
    異步檢查代碼是否已存在於資料庫中。
    """
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.execute('SELECT 1 FROM generated_codes WHERE code = ?', (code,))
        result = await cursor.fetchone()
        return result is not None
    
async def save_code(code):
    """
    異步將代碼儲存到資料庫中。
    """
    async with aiosqlite.connect(db_name) as db:
        try:
            await db.execute('INSERT INTO generated_codes (code) VALUES (?)', (code,))
            await db.commit()
            return True # 儲存成功
        except aiosqlite.IntegrityError:
            # 如果嘗試插入重複的 UNIQUE 值，會觸發 IntegrityError
            logger.error(f"Code '{code}' already exists (IntegrityError).")
            return False # 儲存失敗，因為重複