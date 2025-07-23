# Тестируем микросервисную архитектуру

Смотрю уроки на youtube

 1. [Урок 1](https://www.youtube.com/watch?v=p5kOepy6aZ8&t=221s)

 2. [Урок 2](https://www.youtube.com/watch?v=hgQ2XneUuT8)


Создам два микросрвиса и заставлю взаимодействовать. При чем дуду использовать ключ авторизации также использую Fast API, 
.env. Автоматически будет создана документация в [http://localhost:8002/docs#/]

## Вот создаем requirements.txt

pip freeze > requirements.txt

```bash
    pip freeze > requirements.txt
```

## Вот устанавливаем зависимости

```bash
    pip install -r requirements.txt
```


## Сервис1 .env

```
# Конфигурация Сервиса 1
SERVICE1_API_KEY=service1-secret-key-123
SERVICE2_API_KEY=service2-secret-key-456  # Ключ для доступа к Сервису 2
SERVICE2_URL=http://localhost:8003

# Настройки сервера
HOST=0.0.0.0
PORT=8002
REQUEST_TIMEOUT=5.0
```

## Сервис2 .env

```
# Конфигурация Сервиса 2
SERVICE2_API_KEY=service2-secret-key-456  # Должен совпадать с SERVICE2_API_KEY в Сервисе 1

# Настройки сервера
HOST=0.0.0.0
PORT=8003
REQUEST_TIMEOUT=5.0
```

