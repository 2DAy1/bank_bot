import asyncio
from faker import Faker
from db.async_db import init_db

fake = Faker()


# Генеруємо фейкові дані клієнтів
async def generate_fake_clients(num_clients: int):
    """Генерує фейкових клієнтів та додає їх у таблицю clients"""
    conn = await init_db()
    try:
        for _ in range(num_clients):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()[:20]  # Обрізаємо номер до 20 символів

            await conn.execute(
                'INSERT INTO clients (name, email, phone) VALUES ($1, $2, $3)',
                name, email, phone
            )
        print(f"Успішно додано {num_clients} фейкових клієнтів.")
    finally:
        await conn.close()


# Генеруємо фейкові дані кредитів
async def generate_fake_credits(num_credits: int, num_clients: int):
    """Генерує фейкові кредити для випадкових клієнтів та додає їх у таблицю credits"""
    conn = await init_db()
    try:
        for _ in range(num_credits):
            amount = round(fake.random_number(digits=5), 2)  # Генеруємо суму кредиту
            currency = fake.currency_code()  # Генеруємо код валюти (наприклад, USD, EUR)
            client_id = fake.random_int(min=1, max=num_clients)  # Випадковий клієнт

            await conn.execute(
                'INSERT INTO credits (amount, currency, client_id) VALUES ($1, $2, $3)',
                amount, currency, client_id
            )
        print(f"Успішно додано {num_credits} фейкових кредитів.")
    finally:
        await conn.close()


# Головна функція для генерації тестових даних
async def main():
    num_clients = 10  # Кількість клієнтів
    num_credits = 15  # Кількість кредитів

    # Генеруємо клієнтів і кредити
    await generate_fake_clients(num_clients)
    await generate_fake_credits(num_credits, num_clients)


if __name__ == '__main__':
    asyncio.run(main())
