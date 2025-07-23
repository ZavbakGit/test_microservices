import requests

url = "http://localhost:8002/to-service-2"
headers = {"X-API-Key": "secret-key-123"}

response = requests.get(url, headers=headers)
print(response.json())


# curl -X GET "http://localhost:8002/to-service-2" -H "X-API-Key: service1-secret-key-123"