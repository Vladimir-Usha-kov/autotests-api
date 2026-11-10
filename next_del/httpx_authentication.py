

import httpx

auth_payload = {
    "email": "user1@example.com",
    "password": "22"
}

auth_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=auth_payload)
auth_response_data = auth_response.json()
print("Login response:", auth_response_data)
print("Login Status code:", auth_response.status_code)


refresh_payload = {"refreshToken": auth_response_data["token"]["refreshToken"]}
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print("Refresh response:", refresh_response_data)
print("Refresh status code", refresh_response.status_code)