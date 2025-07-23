import requests


def check_service_availability(url: str) -> bool:
    try:
        response = requests.get(url, timeout=5)  # Добавил таймаут
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False
