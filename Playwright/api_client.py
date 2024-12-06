import requests
import os

BASE_URL = os.getenv("API_BASE_URL", "https://api.club-administration.qa.qubika.com/swagger-ui/index.html#/")

def create_user(registerUser):
    response = requests.post(f"{BASE_URL}/users", json=registerUser)
    response.raise_for_status()
    return response.json()
