import httpx

from tools.fakers import fake

create_users_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_users_response = httpx.post('http://localhost:8000/api/v1/users', json=create_users_payload)
create_users_data = create_users_response.json()
print('Create user response:', create_users_data)
print('Create user response status code:', create_users_response.status_code)


login_payload = {
    "email": create_users_payload['email'],
    "password": create_users_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Login Status code:", login_response.status_code)

headers = {'Authorization': f'bearer {login_response_data['token']['accessToken']}'}

update_user_payload = {
  "email": fake.email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

update_user_response = httpx.patch(
    f'http://localhost:8000/api/v1/users/{create_users_data['user']['id']}',
    json=update_user_payload,
    headers=headers)

update_user_data = update_user_response.json()
print('Update data:',update_user_data)
print('Update status code:',update_user_response.status_code)