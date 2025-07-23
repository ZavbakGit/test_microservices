import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv

app = FastAPI()
port = 8003

# Конфигурация
TIMEOUT = 5.0

load_dotenv()  # Загружает .env из текущей директории
API_KEY = os.getenv("SERVICE2_API_KEY", "service2-key-456")  # Ключ для этого сервиса

# Настройка аутентификации
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)


async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/to-service-2")
async def call_service_2(api_key: str = Depends(verify_api_key)):
    """
    Эндпоинт для взаимодействия с сервисом 2
    """
    return {"response": "I am service 2"}


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == '__main__':
    start_server()
    print(f'Service 2 is running on port {port}')
