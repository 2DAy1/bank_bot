import argparse
import asyncio
import subprocess
from bot.main import run_telegram_bot


def run_fastapi():
    """Запуск FastAPI сервера через uvicorn."""
    subprocess.run(["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Запуск сервісів: Telegram-бота, FastAPI або обох.")
    parser.add_argument("--service", choices=["bot", "api", "both"], default="both",
                        help="Оберіть сервіс для запуску: bot (Telegram-бот), api (FastAPI), both (обидва).")

    args = parser.parse_args()

    if args.service == "bot":
        print("Запускаємо Telegram-бот...")
        asyncio.run(run_telegram_bot())

    elif args.service == "api":
        print("Запускаємо FastAPI сервер...")
        run_fastapi()

    elif args.service == "both":
        print("Запускаємо обидва сервіси...")
        loop = asyncio.get_event_loop()
        loop.create_task(run_telegram_bot())
        run_fastapi()
