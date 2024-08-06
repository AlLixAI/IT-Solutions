import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from src.database import engine, Base  # Импорт функции для инициализации базы данных

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def main():
    # Запускаем инициализацию базы данных
    await init_db()

if __name__ == "__main__":
    asyncio.run(main())