import pytest
from api_client import create_user

@pytest.mark.api
def test_create_user():
    registerUser = {
        "email": "testuser@gmail.com",
        "password": "Test1234!",

    }
    new_user = create_user(registerUser)
    assert "id" in new_user, "The user was created successfully"
    print("User Created:", new_user)