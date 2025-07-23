import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader
import requests
import os
from common.utils import check_service_availability
from dotenv import load_dotenv

app = FastAPI()
port = 8002

# Конфигурация
SERVICE_2_URL = 'http://localhost:8003'
TIMEOUT = 5.0

load_dotenv()  # Загружает .env из текущей директории
API_KEY = os.getenv("SERVICE1_API_KEY", "secret-key-123")  # Ключ для этого сервиса
SERVICE_2_API_KEY = os.getenv("SERVICE2_API_KEY", "service2-key-456")  # Ключ для сервиса 2
print(f"Server expects API_KEY: {API_KEY}")



# Настройка аутентификации
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)


async def verify_api_key(api_key: str = Security(api_key_header)):
    print(f"Received key: '{api_key}'")  # Добавьте для отладки
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/to-service-2")
async def call_service_2(api_key: str = Depends(verify_api_key)):
    """
    Эндпоинт для взаимодействия с сервисом 2
    """
    if not check_service_availability(SERVICE_2_URL):
        raise HTTPException(
            status_code=503,
            detail="Service 2 is unavailable"
        )

    try:
        headers = {"X-API-Key": SERVICE_2_API_KEY}
        response = requests.post(
            f'{SERVICE_2_URL}/to-service-2',
            headers=headers,
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return {"response": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=502,
            detail=f"Error communicating with Service 2: {str(e)}"
        )


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == '__main__':
    start_server()
    print(f'Service 1 is running on port {port}')
