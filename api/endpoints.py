from fastapi import APIRouter
from db.async_db import fetch_client, fetch_credit

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "API is running"}

# Ендпоінт для отримання даних клієнта
@router.get("/client/{client_id}")
async def get_client(client_id: int):
    client_data = await fetch_client(client_id)
    return client_data if client_data else {"error": "Client not found"}


# Ендпоінт для отримання даних про кредит
@router.get("/credit/{credit_id}")
async def get_credit(credit_id: int):
    credit_data = await fetch_credit(credit_id)
    return credit_data if credit_data else {"error": "Credit not found"}

@router.get("/manager/{manager_id}")
async def get_manager(manager_id: int):
    # Логіка для отримання інформації про менеджера з бази
    return {"manager_id": manager_id, "name": "Jane Doe"}
