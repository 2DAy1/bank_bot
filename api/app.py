from fastapi import FastAPI
from api.endpoints import router as api_router
from settings import BANK_NAME  # Імпортуємо налаштування банку

app = FastAPI()

# Додаємо маршрути з endpoints.py
app.include_router(api_router)

@app.get("/")
async def read_root():
    return {"message": f"Welcome to {BANK_NAME} Telegram Bot API!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
