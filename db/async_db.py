import asyncpg
from settings import DATABASE_URL

# Підключення до бази даних
async def init_db():
    """Підключення до бази даних"""
    return await asyncpg.connect(DATABASE_URL)

# Отримання інформації про клієнта з бази даних
async def fetch_client(client_id: int):
    """Отримання даних клієнта за його ID з бази даних"""
    conn = await init_db()
    try:
        result = await conn.fetchrow('SELECT * FROM clients WHERE id = $1', client_id)
    finally:
        await conn.close()
    return result

# Отримання інформації про кредит з бази даних
async def fetch_credit(credit_id: int):
    """Отримання даних про кредит за його ID з бази даних"""
    conn = await init_db()
    try:
        result = await conn.fetchrow('SELECT * FROM credits WHERE id = $1', credit_id)
    finally:
        await conn.close()
    return result
